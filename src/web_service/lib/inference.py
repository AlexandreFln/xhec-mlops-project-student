from typing import List

# import numpy as np
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator

from .models import AgeInput
from .preprocessing import extract_x_y


def run_inference(model: BaseEstimator, input_data: List[AgeInput]) -> int:
    """Run inference on a list of AgeInput objects."""
    logger.info("Running inference")
    df = pd.DataFrame([input.dict() for input in input_data])
    x, _ = extract_x_y(df)
    y = model.predict(x)
    logger.info(f"Predictions: {y}")
    return y
