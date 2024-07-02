import logging
from typing import List, Sequence

import cv2
import numpy as np
import pandas as pd
from flytekit import task


@task
def extract_features(image_data: np.ndarray) -> List[Sequence[float]]:
    """
    Extract features from images. In this case, mean color values are extracted.

    Args:
        image_data (np.ndarray): Array of images.

    Returns:
        list: List of feature tuples containing mean color values (B, G, R).
    """
    logging.info("Extracting image features")

    features = []
    for img in image_data:
        mean_color = cv2.mean(img)[:3]  # Mean color values (B, G, R)
        features.append(mean_color)
    return features


@task
def create_dataframe(
    features: List[Sequence[float]], labels: List[str]
) -> pd.DataFrame:
    """
    Create a pandas DataFrame from extracted features and labels.

    Args:
        features (list): List of feature tuples.
        labels (list): List of image labels.

    Returns:
        pd.DataFrame: DataFrame containing features and labels.
    """
    logging.info("Extracting image dataframe")

    df = pd.DataFrame(features, columns=["mean_blue", "mean_green", "mean_red"])
    df["label"] = labels
    return df
