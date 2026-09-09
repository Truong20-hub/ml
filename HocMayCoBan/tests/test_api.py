from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200


def test_get_prices_endpoint():
    payload = {"area": 120.5, "rooms": 3, "distance": 2.4}
    response = client.post("/get_prices", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert data["status"] == "success"
