import logging
import os
from typing import List

import cv2
import numpy as np
from flytekit import task

from project.crosscutting.utils import create_folder


@task
def extract_frames(
    video_path: str, extract_output_folder: str, frame_rate: int
) -> None:
    """Extract the video frames taking in consideration
    the frame rate and save the multiples images on an
    output folder.

    Args:
    ----
        output_folder (str): Output folder of the extracted frames.
        frame_rate (int): Frame rate to extract the images from video.
    """

    logging.info("Extracting video frames")
    create_folder(extract_output_folder)
    cap = cv2.VideoCapture(video_path)

    count = 0
    success, image = cap.read()

    if not success:
        logging.error("Something went wrong while reading the video.")
        raise ValueError

    while success:
        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_rate == 0:
            cv2.imwrite(
                os.path.join(extract_output_folder, f"frame{count:06d}.jpg"),
                image,
            )
            count += 1
        success, image = cap.read()
    cap.release()


@task
def resize_frames(
    resize_width: int,
    resize_height: int,
    resize_output_folder: str,
    extract_output_folder: str,
) -> (np.ndarray, List[str]):
    """
    Resize extracted frames to the desired size and return a
    tuple of the information for each image and the list of image names.

    Args:
    ----
        size (int, int): width and height to resize the images.
        frame_rate (int): Frame rate to extract the images from video.

    Returns:
    --------
        (np.ndarray, List[str]): Image data information, Image names.
    """
    image_data = []
    image_labels = []

    logging.info("Extracting video frames")
    create_folder(resize_output_folder)

    if not os.path.exists(extract_output_folder):
        logging.error(f"Extract output folder {extract_output_folder} does not exist.")
        raise FileNotFoundError

    for filename in os.listdir(extract_output_folder):
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(extract_output_folder, filename))
            img_resized = cv2.resize(img, (resize_width, resize_height))
            image_data.append(img_resized)
            image_labels.append(filename)
            cv2.imwrite(os.path.join(resize_output_folder, filename), img_resized)

    return np.array(image_data), image_labels
