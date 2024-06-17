import pandas as pd
from fastapi import FastAPI

from product.api.data_model import Items
from product.model.core import Model

app = FastAPI(title="My Model API")

cache = {}


@app.on_event("startup")
def init_model():
    mi = Model()
    mi.load_fitted_model("artifacts")
    cache["Model"] = mi


@app.get("/")
def read_root():
    return "Welcome to the model API!"


@app.post("/predict")
def predict(input: Items):
    input_df = pd.DataFrame.from_records([x.model_dump() for x in input.items])
    predictions = cache["Model"].predict(input_df)
    output_df = pd.DataFrame.from_dict({"prediction": predictions})
    response = output_df.to_dict("records")
    return {"predictions": response}
