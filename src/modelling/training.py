import os

import numpy as np
import pandas as pd
from prefect import flow, task
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split

from src.modelling.predicting import predict
from src.modelling.preprocessing import process_data_flow


@task(name="Train model")
def create_and_train_model(x: pd.DataFrame, y: np.ndarray, **params) -> RandomForestRegressor:
    """Train and return a RandomForestRegressor model with parameters **params."""
    if params is None:
        params = {}
    return RandomForestRegressor(**params).fit(x, y)


# We added this function in case we want to evaluate the model
@task(name="Evaluate model")
def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate mean squared error for two arrays."""
    return root_mean_squared_error(y_true, y_pred)


@flow(name="Train model workflow")
def train_model_workflow(filepath, model, **params) -> dict:
    """Workflow to train model and calculate its Root Mean Squared Error."""
    x, y = process_data_flow(filepath)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    model = create_and_train_model(x_train, y_train, **params)
    y_pred = predict(x_test, model)
    rmse = evaluate_model(y_test, y_pred)

    return {"model": model, "rmse": rmse}


if __name__ == "__main__":

    train_model_workflow(
        os.path.join("src", "data", "abalone.csv"),
    )
