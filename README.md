# Machine Learning Based Product

This repository showcases how a generic machine learning based product could be structured.

## Pipelines

The `make` targets below approximate builds of essential MLOps CI/CD jobs:

```bash
make build-pipe
make training-pipe ARGS='--n_obs 123'
make deploy-pipe RUN_ID=37d75af6d11c44eebbd3e1c9ee3924c6
```

