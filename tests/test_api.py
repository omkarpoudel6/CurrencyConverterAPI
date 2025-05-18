from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_convert():
    response = client.get("/convert?from=USD&to=EUR&amoung=100")
    assert response.status_code == 200
    data = response.json()
    assert "converted_amount" in data 