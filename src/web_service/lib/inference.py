from typing import List

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator

from lib.models import AgeInput
from lib.preprocessing import encode_categorical_cols, extract_x_y


def run_inference(model: BaseEstimator, input_data: List[AgeInput]) -> List[int]:
    """Run inference on a list of AgeInput objects."""
    logger.info("Running inference")
    df = pd.DataFrame([input.dict() for input in input_data])
    df = encode_categorical_cols(df)
    x, _ = extract_x_y(df)
    y = model.predict(x).tolist()
    logger.info(f"Predictions: {y}")
    return y
