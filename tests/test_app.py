import pytest
from app.app import app  # Ensure we're importing the app instance from app.app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.get_json() == []


def test_add_todo(client):
    response = client.post('/todos', json={'todo': 'Test Todo'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Todo added!'

# Ensure the file ends with a blank line
