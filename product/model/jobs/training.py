#!/usr/bin/env python

import logging
from math import ceil

import click
import mlflow

from ...utils.get_data import simulate_data
from ..core import ModelInterface


@click.command()
@click.option("--n_obs", type=int, default=5000, help="Number of simulated observations.")
@click.option(
    "--dont_log_model_artifacts",
    is_flag=True,
    default=False,
    show_default=True,
    help="Dont log model artifacts",
)
def run(n_obs: int, dont_log_model_artifacts: bool) -> str:
    """Run model training, evaluate performance and log to MLFlow."""
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    logger.info("Running training job")

    with mlflow.start_run() as run:
        # get data and train model
        m = ModelInterface()
        y_train, x_train = simulate_data(n=n_obs, sigma=1e3)
        y_test, x_test = simulate_data(n=ceil(n_obs * 0.3), sigma=1e3)
        m.train(x_train, y_train)

        # evaluate model performance
        train_rmse = m.evaluate_performance(x_train, y_train)
        test_rmse = m.evaluate_performance(x_test, y_test)

        # log metrics, metadata and artifacts to MLFlow
        logger.info("Logging model and metadata to MLFlow")
        mlflow.log_metric("train_rmse", train_rmse)
        mlflow.log_metric("test_rmse", test_rmse)
        mlflow.log_param("n_obs", n_obs)
        if not dont_log_model_artifacts:
            mlflow.sklearn.log_model(m.model, "model")

        return run.info.run_id


if __name__ == "__main__":
    run()
