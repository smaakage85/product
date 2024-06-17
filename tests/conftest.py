import numpy as np
import pytest

from product.model.core import Model


@pytest.fixture(autouse=True)
def change_test_dir(tmp_path, monkeypatch):
    """Change working directory for all tests."""
    monkeypatch.chdir(tmp_path)


@pytest.fixture
def mock_model(monkeypatch):
    def mock_load_fitted_model(*args, **kwargs):
        return None

    def mock_predict(self, df):
        return np.random.rand(len(df))

    monkeypatch.setattr(Model, "load_fitted_model", mock_load_fitted_model)
    monkeypatch.setattr(Model, "predict", mock_predict)
