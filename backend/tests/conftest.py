import pytest
import requests
import os

@pytest.fixture
def api_client():
    """Shared requests session"""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session

@pytest.fixture
def base_url():
    """Base URL from environment"""
    # Try multiple environment variable names
    url = os.environ.get('EXPO_PUBLIC_BACKEND_URL') or os.environ.get('EXPO_BACKEND_URL')
    if not url:
        # Load from frontend .env file
        from pathlib import Path
        env_file = Path('/app/frontend/.env')
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    if line.startswith('EXPO_PUBLIC_BACKEND_URL='):
                        url = line.split('=', 1)[1].strip()
                        break
    if not url:
        pytest.fail("EXPO_PUBLIC_BACKEND_URL not found in environment or .env file")
    return url.rstrip('/')
