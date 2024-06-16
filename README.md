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
    - save artifacts
- rename ModelInterface (to just "Model"?)
- rename ModelInterface-methods - `load_model`, `format_input`
- rename `jobs` -> `scripts`
- downloaded/copied model artifacts stored in `.artifacts`
- ruff-configuration in pyproject.toml
- switch to non-root user i Dockerfile
- forbedring af tests til API
    - client(TestAPI)
    - tests til read root metode fra `fastapi` dokumentation
- rename integrations-tests til e2e-tests?
- Add CODEOWNERS
- automatic versioning
- unlock dependencies
- unit test for `load_model`
- move version and package name to .env file
- replace `click` with `typer`?
- replace `mlflow` with `neptune-ai`?
- test package dependencies