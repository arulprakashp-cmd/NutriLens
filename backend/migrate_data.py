"""
Database migration script to:
1. Replace em-dashes with hyphens in all content
2. Split checklist from summary cards into separate cards
3. Update card counts
"""
import asyncio
import os
import json
import re
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

def replace_dashes_recursive(obj):
    """Replace em-dashes and en-dashes with hyphens in all strings"""
    if isinstance(obj, str):
        return obj.replace('\u2014', ' - ').replace('\u2013', '-').replace(' — ', ' - ').replace('—', ' - ')
    elif isinstance(obj, dict):
        return {k: replace_dashes_recursive(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_dashes_recursive(item) for item in obj]
    return obj

async def migrate():
    topics = await db.topics.find().to_list(100)
    
    for topic in topics:
        cards = topic.get('cards', [])
        new_cards = []
        
        for card in cards:
            # Replace dashes in all card content
            card = replace_dashes_recursive(card)
            
            # Check if this is a summary card with a checklist
            if card.get('content', {}).get('type') == 'summary' and card.get('content', {}).get('checklist'):
                checklist = card['content'].pop('checklist')
                new_cards.append(card)
                
                # Create new checklist card
                current_order = card['order']
                checklist_card = {
                    "card_id": f"{topic['key']}_checklist",
                    "number": f"{int(card['number']) + 1:02d}",
                    "label": "Action Checklist",
                    "icon": "📋",
                    "title": "Your Action Plan",
                    "order": current_order + 1,
                    "content": {
                        "type": "checklist",
                        "body": "Start with these simple steps today. Small changes lead to big results.",
                        "checklist": checklist
                    }
                }
                new_cards.append(checklist_card)
            else:
                new_cards.append(card)
        
        # Replace dashes in topic-level fields too
        topic_updates = replace_dashes_recursive({
            "title": topic.get("title", ""),
            "subtitle": topic.get("subtitle", ""),
            "description": topic.get("description", ""),
        })
        
        new_card_count = len(new_cards)
        
        await db.topics.update_one(
            {"_id": topic["_id"]},
            {"$set": {
                "cards": new_cards,
                "card_count": new_card_count,
                **topic_updates,
            }}
        )
        print(f"Updated {topic['key']}: {len(cards)} -> {new_card_count} cards")
    
    print("Migration complete!")

asyncio.run(migrate())
client.close()
