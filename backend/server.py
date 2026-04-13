from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from typing import List
from models import Topic, TopicSummary, Card, ShareCard
from seed_data import TOPICS_DATA


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Collections
topics_collection = db.topics

# Create the main app
app = FastAPI()
api_router = APIRouter(prefix="/api")


# Seed database on startup
@app.on_event("startup")
async def seed_database():
    """Seed the database with nutrition topics if empty"""
    count = await topics_collection.count_documents({})
    if count == 0:
        logger.info("Seeding database with nutrition topics...")
        for topic_data in TOPICS_DATA:
            await topics_collection.insert_one(topic_data)
        logger.info(f"Seeded {len(TOPICS_DATA)} topics successfully!")
    else:
        logger.info(f"Database already contains {count} topics, skipping seed.")


# API Endpoints
@api_router.get("/topics", response_model=List[TopicSummary])
async def get_all_topics():
    """Get all topics summary for home screen"""
    try:
        topics = await topics_collection.find().sort("order", 1).to_list(100)
        return [
            TopicSummary(
                topic_id=topic["topic_id"],
                key=topic["key"],
                title=topic["title"],
                description=topic["description"],
                icon_name=topic["icon_name"],
                emoji=topic["emoji"],
                background_color=topic["background_color"],
                card_count=topic["card_count"],
                order=topic["order"]
            )
            for topic in topics
        ]
    except Exception as e:
        logger.error(f"Error fetching topics: {e}")
        raise HTTPException(status_code=500, detail="Error fetching topics")


@api_router.get("/topics/{topic_key}", response_model=Topic)
async def get_topic_by_key(topic_key: str):
    """Get specific topic with all cards"""
    try:
        topic = await topics_collection.find_one({"key": topic_key})
        if not topic:
            raise HTTPException(status_code=404, detail=f"Topic '{topic_key}' not found")
        
        return Topic(**topic)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching topic {topic_key}: {e}")
        raise HTTPException(status_code=500, detail="Error fetching topic")


@api_router.get("/cards/{card_id}", response_model=Card)
async def get_card_by_id(card_id: str):
    """Get individual card (for sharing)"""
    try:
        # Find topic containing this card
        topic = await topics_collection.find_one({"cards.card_id": card_id})
        if not topic:
            raise HTTPException(status_code=404, detail=f"Card '{card_id}' not found")
        
        # Find the specific card
        card = next((c for c in topic["cards"] if c["card_id"] == card_id), None)
        if not card:
            raise HTTPException(status_code=404, detail=f"Card '{card_id}' not found")
        
        return Card(**card)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching card {card_id}: {e}")
        raise HTTPException(status_code=500, detail="Error fetching card")


@api_router.get("/share/{card_id}", response_model=ShareCard)
async def get_share_card(card_id: str):
    """Get formatted card data for sharing"""
    try:
        # Find topic containing this card
        topic = await topics_collection.find_one({"cards.card_id": card_id})
        if not topic:
            raise HTTPException(status_code=404, detail=f"Card '{card_id}' not found")
        
        # Find the specific card
        card = next((c for c in topic["cards"] if c["card_id"] == card_id), None)
        if not card:
            raise HTTPException(status_code=404, detail=f"Card '{card_id}' not found")
        
        # Format content for sharing
        content_text = f"{card['title']}\n\n{card['content'].get('body', '')}"
        
        return ShareCard(
            card_id=card_id,
            topic_title=topic["title"],
            card_title=card["title"],
            card_number=f"{card['number']} / {card['label']}",
            content_text=content_text
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating share card {card_id}: {e}")
        raise HTTPException(status_code=500, detail="Error creating share card")


# Health check
@api_router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "nutrients-story-api"}


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
