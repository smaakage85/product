import numpy as np
import pandas as pd
import pytest

from product.utils.get_data import simulate_data


@pytest.mark.parametrize(
    "test_input,expected_output",
    [(1, 1), (10, 10)],
)
def test_simulate_data(test_input, expected_output):
    n = test_input
    y, x = simulate_data(n=n)
    assert isinstance(y, np.ndarray)
    assert isinstance(x, pd.DataFrame)
    assert len(y) == len(x) == expected_output
