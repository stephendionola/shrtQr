import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.db_service import execute_query

client = TestClient(app)

# Truncate the links table to ensure clean state for every test
@pytest.fixture(autouse=True)  # This will run before every test
def clean_db():
    execute_query("TRUNCATE TABLE links RESTART IDENTITY CASCADE;")

def test_shorten_url():
    response = client.post("/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    assert "short_code" in response.json()

def test_get_link():
    # Create a shortened URL first
    res = client.post("/shorten", json={"url": "https://example.com"}).json()
    short_code = res['short_code']

    # Retrieve the original URL using the short code
    response = client.get(f"/{short_code}")
    assert response.status_code == 200
    assert response.json()["url"] == "https://example.com"

def test_invalid_short_code():
    response = client.get("/invalid_code")
    assert response.status_code == 404


