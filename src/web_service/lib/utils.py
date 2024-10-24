import os
import pickle
from functools import lru_cache

from loguru import logger

from src.web_service.app_config import PATH_TO_MODEL

filepath = PATH_TO_MODEL


@lru_cache
def load_model(filepath: os.PathLike):
    """Load model from pickle file."""
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)
