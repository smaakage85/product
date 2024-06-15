import mlflow
import pytest
from click.testing import CliRunner
from fastapi.testclient import TestClient
from product import api
from product.model.jobs import training


def test_e2e():
    """Test that a model can be trained and then served through API"""
    # training
    runner = CliRunner()
    result = runner.invoke(training.run, ["--n_obs", 50], standalone_mode=False)
    assert result.exit_code == 0
    assert result.return_value
    run_id = result.return_value
    try:
        mlflow.artifacts.download_artifacts(run_id=run_id, dst_path="artifacts")
    except mlflow.exceptions.MlflowException as e:
        pytest.fail(f"Collecting model artifacts from MLFlow failed: {e}")
    # API
    with TestClient(api) as client:
        response = client.post(
            "/predict/",
            json={"items": [{"age": 20, "skills": 0.3}, {"age": 49, "skills": -0.5}]},
        )
        assert response.status_code == 200
