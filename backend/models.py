from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class Card(BaseModel):
    """Individual information card within a topic"""
    card_id: str
    number: str  # e.g., "01", "02"
    label: str  # e.g., "Reality Check", "Why Protein?"
    icon: str  # emoji icon
    title: str
    content: Dict[str, Any]  # Flexible structure for different card types
    order: int
    translations: Optional[Dict[str, Dict[str, str]]] = None


class Topic(BaseModel):
    """Main topic (Protein, Carbs, Fats)"""
    topic_id: str
    key: str  # "protein", "carbs", "fats"
    title: str  # "The Protein Story"
    subtitle: str
    icon_name: str  # For vector icon
    emoji: str
    background_color: str
    description: str
    card_count: int
    cards: List[Card]
    order: int
    translations: Optional[Dict[str, Dict[str, str]]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TopicSummary(BaseModel):
    """Summary for home screen"""
    topic_id: str
    key: str
    title: str
    description: str
    icon_name: str
    emoji: str
    background_color: str
    card_count: int
    order: int
    translations: Optional[Dict[str, Dict[str, str]]] = None


class ShareCard(BaseModel):
    """Card data formatted for sharing"""
    card_id: str
    topic_title: str
    card_title: str
    card_number: str
    content_text: str
