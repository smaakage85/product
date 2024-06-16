run_tests:
	coverage run -m pytest tests/unit
	coverage report -m

train_model:
	docker run --rm -v ./mlruns:/app/mlruns:rw product train_model