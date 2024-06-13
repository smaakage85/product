import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


def simulate_data(n: int = 1000, sigma: float = 1e3) -> tuple[np.array, pd.DataFrame]:
    """Simulate Salaries Data

    Simulates pairs of the target variable: salary and two features:
    (1) age and (2) skills. Data is generated from a linear process
    with noise.

    Args:
        n (int, optional): Number of observations. Defaults to 1000.
        sigma (float, optional): Noise variance. Defaults to 1e3.

    Returns:
        tuple[np.array, pd.DataFrame]: salaries, features.
    """
    logger.info(f"Simulating {n} observations, sigma={sigma}")
    age = np.random.randint(size=n, low=20, high=70)
    skills = np.random.randn(n)
    e = np.random.randn(n) * sigma
    salary = sigma * np.array(age) + e
    x = pd.DataFrame({"age": age, "skills": skills})
    return salary, x
