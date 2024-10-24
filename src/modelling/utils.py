# Use this module to code a `pickle_object` function. This will be useful to pickle the model (and encoder if need be).
import pickle
from typing import Any


def load_pickle(path: str):
    """Load pickle object."""
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


def save_pickle(path: str, obj: Any):
    """Save pickle object."""
    with open(path, "wb") as f:
        pickle.dump(obj, f)
