lint:
	ruff check

run-tests:
	-rm .coverage
	coverage run -m pytest tests/unit
	coverage report --fail-under=80
	python -m pytest tests/integration tests/e2e

build-package:
	-rm -rf dist
	python -m build

build-image:
	docker build -t product .

build-pipe: lint run-tests build-package build-image

training-pipe:
	python -m product.model.jobs.training ${ARGS}

dl-model-artifacts:
	-rm -rf artifacts
	mlflow artifacts download \
		--run-id ${RUN_ID} \
		--dst-path artifacts

deploy-pipe: dl-model-artifacts
	uvicorn product:api

