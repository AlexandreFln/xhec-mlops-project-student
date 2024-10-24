from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL,
    PATH_TO_PREPROCESSOR,
)
from fastapi import FastAPI

# Other imports
from lib.inference import run_inference
from lib.models import AgeInput, AgeOutput
from lib.utils import load_model, load_preprocessor

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=AgeOutput, status_code=201)
def predict(payload: AgeInput) -> dict:
    model = load_model(PATH_TO_MODEL)
    dv = load_preprocessor(PATH_TO_PREPROCESSOR)
    y = run_inference(model, dv, [payload])
    return {"age": y[0]}
