#!/usr/bin/env python3
"""
Backend API Testing for Nutrients Story API
Tests all endpoints as specified in the review request
"""

import requests
import json
import sys
from typing import Dict, Any, List

# Backend URL from frontend environment
BACKEND_URL = "https://diet-info-app.preview.emergentagent.com/api"

class NutrientsAPITester:
    def __init__(self):
        self.results = []
        self.passed = 0
        self.failed = 0
        
    def log_result(self, test_name: str, passed: bool, details: str = ""):
        """Log test result"""
        status = "✅ PASS" if passed else "❌ FAIL"
        self.results.append(f"{status} {test_name}: {details}")
        if passed:
            self.passed += 1
        else:
            self.failed += 1
            
    def test_health_endpoint(self):
        """Test GET /api/health endpoint"""
        try:
            response = requests.get(f"{BACKEND_URL}/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "healthy":
                    self.log_result("Health Check", True, "Status: healthy")
                else:
                    self.log_result("Health Check", False, f"Unexpected status: {data}")
            else:
                self.log_result("Health Check", False, f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result("Health Check", False, f"Exception: {str(e)}")
            
    def test_topics_endpoint(self):
        """Test GET /api/topics endpoint"""
        try:
            response = requests.get(f"{BACKEND_URL}/topics", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if it's a list
                if not isinstance(data, list):
                    self.log_result("Topics List", False, "Response is not a list")
                    return
                    
                # Check if we have 3 topics
                if len(data) != 3:
                    self.log_result("Topics Count", False, f"Expected 3 topics, got {len(data)}")
                    return
                else:
                    self.log_result("Topics Count", True, "3 topics returned")
                
                # Check topic structure and expected topics
                expected_keys = ["protein", "carbs", "fats"]
                expected_counts = {"protein": 9, "carbs": 12, "fats": 13}
                
                for topic in data:
                    key = topic.get("key")
                    if key not in expected_keys:
                        self.log_result(f"Topic Key {key}", False, "Unexpected topic key")
                        continue
                        
                    # Check required fields
                    required_fields = ["topic_id", "key", "title", "description", "emoji", 
                                     "icon_name", "background_color", "card_count", "order"]
                    
                    missing_fields = [field for field in required_fields if field not in topic]
                    if missing_fields:
                        self.log_result(f"Topic {key} Structure", False, f"Missing fields: {missing_fields}")
                    else:
                        self.log_result(f"Topic {key} Structure", True, "All required fields present")
                        
                    # Check card count
                    actual_count = topic.get("card_count")
                    expected_count = expected_counts.get(key)
                    if actual_count == expected_count:
                        self.log_result(f"Topic {key} Card Count", True, f"{actual_count} cards")
                    else:
                        self.log_result(f"Topic {key} Card Count", False, f"Expected {expected_count}, got {actual_count}")
                        
            else:
                self.log_result("Topics Endpoint", False, f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result("Topics Endpoint", False, f"Exception: {str(e)}")
            
    def test_topic_by_key(self, topic_key: str, expected_card_count: int):
        """Test GET /api/topics/{topic_key} endpoint"""
        try:
            response = requests.get(f"{BACKEND_URL}/topics/{topic_key}", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if topic has correct key
                if data.get("key") != topic_key:
                    self.log_result(f"Topic {topic_key} Key", False, f"Expected key {topic_key}, got {data.get('key')}")
                    return
                else:
                    self.log_result(f"Topic {topic_key} Key", True, f"Correct key: {topic_key}")
                
                # Check if cards are present
                cards = data.get("cards", [])
                if len(cards) == expected_card_count:
                    self.log_result(f"Topic {topic_key} Cards Count", True, f"{len(cards)} cards")
                else:
                    self.log_result(f"Topic {topic_key} Cards Count", False, f"Expected {expected_card_count}, got {len(cards)}")
                    
                # Check card structure for first card
                if cards:
                    card = cards[0]
                    required_card_fields = ["card_id", "number", "label", "icon", "title", "content", "order"]
                    missing_fields = [field for field in required_card_fields if field not in card]
                    if missing_fields:
                        self.log_result(f"Topic {topic_key} Card Structure", False, f"Missing fields: {missing_fields}")
                    else:
                        self.log_result(f"Topic {topic_key} Card Structure", True, "Card structure valid")
                        
            elif response.status_code == 404:
                self.log_result(f"Topic {topic_key}", False, "Topic not found (404)")
            else:
                self.log_result(f"Topic {topic_key}", False, f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result(f"Topic {topic_key}", False, f"Exception: {str(e)}")
            
    def test_card_by_id(self, card_id: str):
        """Test GET /api/cards/{card_id} endpoint"""
        try:
            response = requests.get(f"{BACKEND_URL}/cards/{card_id}", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if card has correct ID
                if data.get("card_id") != card_id:
                    self.log_result(f"Card {card_id} ID", False, f"Expected {card_id}, got {data.get('card_id')}")
                    return
                else:
                    self.log_result(f"Card {card_id} ID", True, f"Correct ID: {card_id}")
                
                # Check card structure
                required_fields = ["card_id", "number", "label", "icon", "title", "content", "order"]
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    self.log_result(f"Card {card_id} Structure", False, f"Missing fields: {missing_fields}")
                else:
                    self.log_result(f"Card {card_id} Structure", True, "All required fields present")
                    
            elif response.status_code == 404:
                self.log_result(f"Card {card_id}", False, "Card not found (404)")
            else:
                self.log_result(f"Card {card_id}", False, f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result(f"Card {card_id}", False, f"Exception: {str(e)}")
            
    def test_share_card(self, card_id: str):
        """Test GET /api/share/{card_id} endpoint"""
        try:
            response = requests.get(f"{BACKEND_URL}/share/{card_id}", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check ShareCard structure
                required_fields = ["card_id", "topic_title", "card_title", "card_number", "content_text"]
                missing_fields = [field for field in required_fields if field not in data]
                if missing_fields:
                    self.log_result(f"Share Card {card_id} Structure", False, f"Missing fields: {missing_fields}")
                else:
                    self.log_result(f"Share Card {card_id} Structure", True, "All required fields present")
                    
                # Check if card_id matches
                if data.get("card_id") != card_id:
                    self.log_result(f"Share Card {card_id} ID", False, f"Expected {card_id}, got {data.get('card_id')}")
                else:
                    self.log_result(f"Share Card {card_id} ID", True, f"Correct ID: {card_id}")
                    
            elif response.status_code == 404:
                self.log_result(f"Share Card {card_id}", False, "Card not found (404)")
            else:
                self.log_result(f"Share Card {card_id}", False, f"HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result(f"Share Card {card_id}", False, f"Exception: {str(e)}")
            
    def run_all_tests(self):
        """Run all API tests"""
        print("🧪 Starting Nutrients Story API Tests...")
        print(f"🔗 Backend URL: {BACKEND_URL}")
        print("=" * 60)
        
        # Test 1: Health check
        self.test_health_endpoint()
        
        # Test 2: Get all topics
        self.test_topics_endpoint()
        
        # Test 3-5: Get individual topics with cards
        self.test_topic_by_key("protein", 9)
        self.test_topic_by_key("carbs", 12)
        self.test_topic_by_key("fats", 13)
        
        # Test 6: Get individual card
        self.test_card_by_id("protein_01")
        
        # Test 7: Get share card
        self.test_share_card("protein_01")
        
        # Print results
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS SUMMARY")
        print("=" * 60)
        
        for result in self.results:
            print(result)
            
        print(f"\n🎯 TOTAL: {self.passed + self.failed} tests")
        print(f"✅ PASSED: {self.passed}")
        print(f"❌ FAILED: {self.failed}")
        
        if self.failed == 0:
            print("\n🎉 ALL TESTS PASSED! Backend API is working correctly.")
            return True
        else:
            print(f"\n⚠️  {self.failed} test(s) failed. Check the details above.")
            return False

if __name__ == "__main__":
    tester = NutrientsAPITester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)