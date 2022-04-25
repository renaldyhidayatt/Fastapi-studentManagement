from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_hello():
    response = client.get("/admin/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
