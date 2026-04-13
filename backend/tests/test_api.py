"""Backend API tests for Nutrients Story app"""
import pytest
import requests


class TestHealthCheck:
    """Health check endpoint tests"""

    def test_health_endpoint(self, api_client, base_url):
        """Test health check endpoint"""
        response = api_client.get(f"{base_url}/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "service" in data


class TestTopicsEndpoint:
    """Tests for /api/topics endpoint"""

    def test_get_all_topics_success(self, api_client, base_url):
        """Test GET /api/topics returns 3 topics"""
        response = api_client.get(f"{base_url}/api/topics")
        assert response.status_code == 200
        
        topics = response.json()
        assert isinstance(topics, list)
        assert len(topics) == 3, f"Expected 3 topics, got {len(topics)}"

    def test_topics_structure(self, api_client, base_url):
        """Test topics have correct structure"""
        response = api_client.get(f"{base_url}/api/topics")
        assert response.status_code == 200
        
        topics = response.json()
        required_fields = ["topic_id", "key", "title", "description", "emoji", 
                          "background_color", "card_count", "order"]
        
        for topic in topics:
            for field in required_fields:
                assert field in topic, f"Missing field '{field}' in topic"

    def test_topics_order(self, api_client, base_url):
        """Test topics are ordered correctly"""
        response = api_client.get(f"{base_url}/api/topics")
        assert response.status_code == 200
        
        topics = response.json()
        keys = [t["key"] for t in topics]
        assert keys == ["protein", "carbs", "fats"], f"Expected order [protein, carbs, fats], got {keys}"

    def test_topics_card_counts(self, api_client, base_url):
        """Test topics have correct card counts"""
        response = api_client.get(f"{base_url}/api/topics")
        assert response.status_code == 200
        
        topics = response.json()
        expected_counts = {"protein": 9, "carbs": 12, "fats": 13}
        
        for topic in topics:
            key = topic["key"]
            assert topic["card_count"] == expected_counts[key], \
                f"Expected {expected_counts[key]} cards for {key}, got {topic['card_count']}"


class TestTopicByKey:
    """Tests for /api/topics/{key} endpoint"""

    def test_get_protein_topic(self, api_client, base_url):
        """Test GET /api/topics/protein returns topic with 9 cards"""
        response = api_client.get(f"{base_url}/api/topics/protein")
        assert response.status_code == 200
        
        topic = response.json()
        assert topic["key"] == "protein"
        assert topic["title"] == "The Protein Story"
        assert len(topic["cards"]) == 9, f"Expected 9 cards, got {len(topic['cards'])}"

    def test_get_carbs_topic(self, api_client, base_url):
        """Test GET /api/topics/carbs returns topic with 12 cards"""
        response = api_client.get(f"{base_url}/api/topics/carbs")
        assert response.status_code == 200
        
        topic = response.json()
        assert topic["key"] == "carbs"
        assert topic["title"] == "The Carbs Story"
        assert len(topic["cards"]) == 12, f"Expected 12 cards, got {len(topic['cards'])}"

    def test_get_fats_topic(self, api_client, base_url):
        """Test GET /api/topics/fats returns topic with 13 cards"""
        response = api_client.get(f"{base_url}/api/topics/fats")
        assert response.status_code == 200
        
        topic = response.json()
        assert topic["key"] == "fats"
        assert topic["title"] == "The Fat Story"
        assert len(topic["cards"]) == 13, f"Expected 13 cards, got {len(topic['cards'])}"

    def test_topic_not_found(self, api_client, base_url):
        """Test GET /api/topics/invalid returns 404"""
        response = api_client.get(f"{base_url}/api/topics/invalid")
        assert response.status_code == 404

    def test_topic_cards_structure(self, api_client, base_url):
        """Test cards in topic have correct structure"""
        response = api_client.get(f"{base_url}/api/topics/protein")
        assert response.status_code == 200
        
        topic = response.json()
        required_fields = ["card_id", "number", "label", "icon", "title", "order", "content"]
        
        for card in topic["cards"]:
            for field in required_fields:
                assert field in card, f"Missing field '{field}' in card"
            assert "type" in card["content"], "Missing 'type' in card content"


class TestCardById:
    """Tests for /api/cards/{card_id} endpoint"""

    def test_get_card_by_id(self, api_client, base_url):
        """Test GET /api/cards/protein_01 returns card"""
        response = api_client.get(f"{base_url}/api/cards/protein_01")
        assert response.status_code == 200
        
        card = response.json()
        assert card["card_id"] == "protein_01"
        assert "title" in card
        assert "content" in card

    def test_get_card_not_found(self, api_client, base_url):
        """Test GET /api/cards/invalid returns 404"""
        response = api_client.get(f"{base_url}/api/cards/invalid_card")
        assert response.status_code == 404


class TestShareCard:
    """Tests for /api/share/{card_id} endpoint"""

    def test_share_protein_card(self, api_client, base_url):
        """Test GET /api/share/protein_01 returns formatted share data"""
        response = api_client.get(f"{base_url}/api/share/protein_01")
        assert response.status_code == 200
        
        share_data = response.json()
        assert share_data["card_id"] == "protein_01"
        assert "topic_title" in share_data
        assert "card_title" in share_data
        assert "card_number" in share_data
        assert "content_text" in share_data
        assert len(share_data["content_text"]) > 0

    def test_share_carbs_card(self, api_client, base_url):
        """Test GET /api/share/carbs_01 returns formatted share data"""
        response = api_client.get(f"{base_url}/api/share/carbs_01")
        assert response.status_code == 200
        
        share_data = response.json()
        assert share_data["card_id"] == "carbs_01"
        assert share_data["topic_title"] == "The Carbs Story"

    def test_share_fats_card(self, api_client, base_url):
        """Test GET /api/share/fats_01 returns formatted share data"""
        response = api_client.get(f"{base_url}/api/share/fats_01")
        assert response.status_code == 200
        
        share_data = response.json()
        assert share_data["card_id"] == "fats_01"
        assert share_data["topic_title"] == "The Fat Story"

    def test_share_card_not_found(self, api_client, base_url):
        """Test GET /api/share/invalid returns 404"""
        response = api_client.get(f"{base_url}/api/share/invalid_card")
        assert response.status_code == 404


class TestCardTypes:
    """Tests for specialized card types and renderers"""

    def test_protein_amino_acids_card(self, api_client, base_url):
        """Test amino_acids card type exists in protein topic"""
        response = api_client.get(f"{base_url}/api/topics/protein")
        assert response.status_code == 200
        
        topic = response.json()
        amino_card = next((c for c in topic["cards"] if c["content"]["type"] == "amino_acids"), None)
        assert amino_card is not None, "amino_acids card not found in protein topic"
        assert "essential" in amino_card["content"]
        assert "non_essential" in amino_card["content"]

    def test_protein_plan_card(self, api_client, base_url):
        """Test protein_plan card type exists"""
        response = api_client.get(f"{base_url}/api/topics/protein")
        assert response.status_code == 200
        
        topic = response.json()
        plan_card = next((c for c in topic["cards"] if c["content"]["type"] == "protein_plan"), None)
        assert plan_card is not None, "protein_plan card not found"

    def test_carbs_gi_chart_card(self, api_client, base_url):
        """Test gi_chart card type exists in carbs topic"""
        response = api_client.get(f"{base_url}/api/topics/carbs")
        assert response.status_code == 200
        
        topic = response.json()
        gi_card = next((c for c in topic["cards"] if c["content"]["type"] == "gi_chart"), None)
        assert gi_card is not None, "gi_chart card not found in carbs topic"

    def test_fats_timeline_card(self, api_client, base_url):
        """Test timeline card type exists in fats topic"""
        response = api_client.get(f"{base_url}/api/topics/fats")
        assert response.status_code == 200
        
        topic = response.json()
        timeline_card = next((c for c in topic["cards"] if c["content"]["type"] == "timeline"), None)
        assert timeline_card is not None, "timeline card not found in fats topic"

    def test_fats_myths_card(self, api_client, base_url):
        """Test myths card type exists in fats topic"""
        response = api_client.get(f"{base_url}/api/topics/fats")
        assert response.status_code == 200
        
        topic = response.json()
        myths_card = next((c for c in topic["cards"] if c["content"]["type"] == "myths"), None)
        assert myths_card is not None, "myths card not found in fats topic"
