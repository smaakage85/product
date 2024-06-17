import numpy as np
import pandas as pd
import pytest

from product.model.core import Model


@pytest.fixture
def input_data():
    x = pd.DataFrame(np.array([[1, 1], [1, 2], [2, 2], [2, 3]]), columns=["age", "height"])
    y = np.dot(x, np.array([1, 2])) + 3
    return x, y


@pytest.fixture
def model():
    model = Model()
    return model


def test_engineer_features(input_data, model):
    x, y = input_data
    x_log = model.engineer_features(x)["log_age"]
    assert x_log.equals(np.log(x["age"]))


def test_train_pred_eval(input_data, model):
    x, y = input_data
    model.train(x, y)
    assert model.model.score(x, y) == 1.0
    assert (model.predict(x) == np.array([6.0, 8.0, 9.0, 11.0])).all()
    assert model.evaluate_performance(x, y) == 0.0
