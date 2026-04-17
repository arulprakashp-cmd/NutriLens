"""Apply all deep structured translations from batches 1-3"""
import asyncio, os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path
from deep_trans_batch1 import PROTEIN_DEEP as _PD
from deep_trans_batch2 import FATS_DEEP, FIBRE_DEEP
from deep_trans_batch3 import VITAMINS_DEEP, HYDRATION_DEEP

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')
client = AsyncIOMotorClient(os.environ['MONGO_URL'])
db = client[os.environ['DB_NAME']]

# Merge all deep translations
ALL_DEEP = {}
ALL_DEEP.update(_PD)  # Contains protein + carbs keys
ALL_DEEP.update(FATS_DEEP)
ALL_DEEP.update(FIBRE_DEEP)
ALL_DEEP.update(VITAMINS_DEEP)
ALL_DEEP.update(HYDRATION_DEEP)

async def apply():
    all_topics = await db.topics.find().to_list(100)
    updated = 0
    for topic in all_topics:
        cards = topic.get("cards", [])
        changed = False
        for card in cards:
            cid = card.get("card_id", "")
            if cid in ALL_DEEP:
                dt = ALL_DEEP[cid]
                if "translations" not in card:
                    card["translations"] = {}
                for lang in ["ta", "hi"]:
                    if lang not in card["translations"]:
                        card["translations"][lang] = {}
                    if lang in dt:
                        card["translations"][lang].update(dt[lang])
                changed = True
                updated += 1
        if changed:
            await db.topics.update_one({"_id": topic["_id"]}, {"$set": {"cards": cards}})
            print(f"  Updated {topic['key']}")
    
    # Print coverage stats
    total_cards = 0
    translated_cards = 0
    for topic in await db.topics.find().to_list(100):
        for card in topic.get("cards", []):
            total_cards += 1
            t = card.get("translations", {})
            ta = t.get("ta", {})
            if len(ta) > 2:  # has more than just title+body
                translated_cards += 1
    
    print(f"\nApplied deep translations to {updated} cards")
    print(f"Cards with deep structured translations: {translated_cards}/{total_cards}")
    print("Done!")

asyncio.run(apply())
client.close()
ose()
