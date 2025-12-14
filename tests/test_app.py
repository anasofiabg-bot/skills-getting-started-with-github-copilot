import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_remove_participant():
    # Crear una actividad temporal para el test
    activity_name = "TestActivity"
    email = "testuser@example.com"
    activities[activity_name] = {
        "description": "Actividad de prueba",
        "schedule": "Lunes 10:00",
        "max_participants": 5,
        "participants": []
    }
    # Signup
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200
    # Remove
    response = client.delete(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200
    # Limpieza
    del activities[activity_name]
