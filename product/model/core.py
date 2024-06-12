import logging
import math
import os
from dataclasses import dataclass
from typing import Optional

import mlflow
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

logger = logging.getLogger(__name__)


@dataclass
class ModelInterface:
    """Model Interface.

    Interface with basic methods for implementing a ML model.

    Args:
        model (LinearRegression): Linear model.
    """

    model: Optional[LinearRegression] = None

    def format_input(self, x: pd.DataFrame) -> pd.DataFrame:
        """Conduct feature engineering etcetera.

        Args:
            x (pd.DataFrame): Initial features.

        Returns:
            pd.DataFrame: Finalized features.
        """
        logger.info("Formatting input")
        x["log_age"] = np.log(x["age"])
        logger.info("Formatting done.")
        return x

    def train(self, x: pd.DataFrame, y: np.ndarray) -> None:
        """Train model.

        Args:
            x (pd.DataFrame): Features.
            y (np.ndarray): Target (=Salaries).
        """
        lr = LinearRegression()
        logger.info("Training model")
        x = self.format_input(x)
        lr.fit(x, y)
        logger.info("Training done.")
        self.model = lr

    def predict(self, x: pd.DataFrame) -> np.ndarray:
        """Predict observations.

        Args:
            x (pd.DataFrame): Features.

        Returns:
            np.ndarray: Predictions.
        """
        x = self.format_input(x)
        preds = self.model.predict(x)
        return preds

    def evaluate_performance(self, x: pd.DataFrame, y: np.ndarray) -> float:
        """Evaluate model performance.

        Args:
            x (pd.DataFrame): Features.
            y (np.ndarray): Target.

        Returns:
            float: Value of performance metric.
        """
        logger.info("Evaluating model")
        y_pred = self.predict(x)
        rmse = math.sqrt(mean_squared_error(y, y_pred))
        logger.info(f"rmse = {rmse}")
        return rmse

    def load_model_artifacts(self, dir: str = "artifacts") -> None:
        """Load model from MLFlow model training artifacts

        Args:
            dir (str, optional): Directory with MLFlow model
              artifacts. Defaults to "artifacts".
        """
        self.model = mlflow.sklearn.load_model(os.path.join(dir, "model"))
