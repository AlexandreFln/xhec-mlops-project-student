from fastapi import FastAPI

from .app_config import (  # MODEL_VERSION,; PATH_TO_MODEL,; PATH_TO_PREPROCESSOR,
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
)

# Other imports
from .lib.inference import run_inference
from .lib.models import AgeInput, AgeOutput
from .lib.utils import load_model

app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home() -> dict:
    """Home route."""
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=AgeOutput, status_code=201)
def predict(payload: AgeInput) -> dict:
    """Predict the age of an abalone shellfish."""
    import os

    # Imprimer le répertoire de travail courant
    print("Current working directory:", os.getcwd())

    # Vérifier si le fichier existe
    file_path_test = "local_models/model__v0.0.1.pkl"
    if os.path.exists(file_path_test):
        print(f"File '{file_path_test}' exists.")
    else:
        print(f"File '{file_path_test}' does not exist.")
    model = load_model(file_path_test)
    y = run_inference(model, [payload])
    return {"age": y}
