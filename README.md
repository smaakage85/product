# My Machine Learning Based Product

## Testing

Unit tests 

```bash
coverage run -m pytest tests/unit
coverage report
```

## TO-DO
- rename training job
- html reports from `pytest` and `coverage`
- rename ModelInterface (to just "Model"?)
- pip cache requirements*.txt
- rename ModelInterface-methods - `load_model`, `format_input`
- ruff configuration in pyproject.toml
- Add CODEOWNERS
- automatic versioning
- unlock dependencies
- unit test for `load_model`
- move version and package name to .env file
- replace `click` with `typer`?
- replace `mlflow` with `neptune-ai`?
- test package dependencies
