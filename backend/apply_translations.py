"""Apply all card translations (Tamil & Hindi) to MongoDB"""
import asyncio, os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pathlib import Path
from translations_part1 import PROTEIN_TRANSLATIONS, CARBS_TRANSLATIONS, FATS_TRANSLATIONS
from translations_part2 import FIBRE_TRANSLATIONS, VITAMINS_TRANSLATIONS, HYDRATION_TRANSLATIONS

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')
client = AsyncIOMotorClient(os.environ['MONGO_URL'])
db = client[os.environ['DB_NAME']]

ALL_TRANSLATIONS = {
    "protein": PROTEIN_TRANSLATIONS,
    "carbs": CARBS_TRANSLATIONS,
    "fats": FATS_TRANSLATIONS,
    "fibre": FIBRE_TRANSLATIONS,
    "vitamins": VITAMINS_TRANSLATIONS,
    "hydration": HYDRATION_TRANSLATIONS,
}

async def apply_translations():
    for topic_key, translations in ALL_TRANSLATIONS.items():
        topic = await db.topics.find_one({"key": topic_key})
        if not topic:
            print(f"Topic '{topic_key}' not found, skipping")
            continue

        # Apply topic-level translations
        topic_trans = translations.get("topic", {})
        
        # Apply card-level translations
        cards = topic.get("cards", [])
        updated_cards = []
        for card in cards:
            card_id = card.get("card_id", "")
            card_trans = translations.get(card_id, {})
            if card_trans:
                card["translations"] = card_trans
            updated_cards.append(card)

        await db.topics.update_one(
            {"key": topic_key},
            {"$set": {
                "translations": topic_trans,
                "cards": updated_cards,
            }}
        )
        card_count = sum(1 for c in updated_cards if "translations" in c)
        print(f"Updated '{topic_key}': topic translations + {card_count} card translations")

    print("\nAll translations applied!")

asyncio.run(apply_translations())
client.close()
