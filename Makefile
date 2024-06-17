run_tests:
	coverage run -m pytest tests/unit
	coverage report -m

dl_model_artifacts:
	mlflow artifacts download --run-id ooo --dst-path artifacts

