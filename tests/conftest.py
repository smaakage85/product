import pytest


@pytest.fixture(autouse=True)
def change_test_dir(tmp_path, monkeypatch):
    """Change working directory for all tests."""
    monkeypatch.chdir(tmp_path)
