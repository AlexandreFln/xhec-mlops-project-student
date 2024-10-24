import argparse
from pathlib import Path

import pandas as pd
from preprocessing import encode_categorical_cols, extract_x_y
from training import create_and_train_model
from utils import save_pickle


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    df = pd.read_csv(trainset_path)
    # Preprocess data
    df = encode_categorical_cols(df)
    x, y = extract_x_y(df)
    # (Optional) Pickle encoder if need be
    # Train model
    model = create_and_train_model(x, y)

    # Pickle model --> Save the model in the pkl format in the specified folder
    save_pickle("../web_service/local_objects", model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
