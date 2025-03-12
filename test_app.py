import pytest
from app import run, run2, app

def test_run():
    assert run() == "works"

def test_run2_num():
    """Test that run2 function correctly adds two numbers"""
    assert run2(2, 3) == 5
    assert run2(-1, 1) == 0
    assert run2(0, 0) == 0

def test_run2_string():
    """Test that run2 function correctly concatenates strings"""
    assert run2("hello ", "world") == "hello world"

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the root endpoint returns 'works'"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "works"