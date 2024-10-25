import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.db_service import execute_query

client = TestClient(app)

# Truncate the links table to ensure clean state for every test
@pytest.fixture(autouse=True)  # This will run before every test
def clean_db():
    execute_query("TRUNCATE TABLE links RESTART IDENTITY CASCADE;")

def test_create_user():
    pass

def test_get_user():
    pass

def test_delete_user():
    pass

def test_update_user():
    pass

def test__user():
    pass

