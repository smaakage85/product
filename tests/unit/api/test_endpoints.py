from fastapi.testclient import TestClient

from product import api


def test_endpoints(mock_model):
    with TestClient(api) as client:
        response = client.get("/")
        assert response.status_code == 200
        response = client.post(
            "/predict/",
            json={"items": [{"age": 20, "skills": 0.3}, {"age": 49, "skills": -0.5}]},
        )
        assert response.status_code == 200
