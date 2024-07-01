import pandas as pd
from flytekit import workflow

from project.create_dataset import create_dataframe, extract_features
from project.video_extract import extract_frames, resize_frames


@workflow
def video_to_images_workflow(
    video_path: str, resize_width: int, resize_height: int, frame_rate: int
) -> pd.DataFrame:
    """
    Generate an image dataset by extracting and resizing frames from a video.

    Args:
    ----
        video_path (str): Video path to generate the dataset.
        resize_width (int): Desired width size of the output images.
        resize_height (int): Desired width size of the output images.
        frame_rate(int): Image frame rate per second.
    """
    extract_frames(
        video_path=video_path,
        extract_output_folder="dataset/frames",
        frame_rate=frame_rate,
    )

    image_data, image_labels = resize_frames(
        resize_width=resize_width,
        resize_height=resize_height,
        resize_output_folder="dataset/resize_frames",
        extract_output_folder="dataset/frames",
    )

    features = extract_features(image_data=image_data)

    df = create_dataframe(features=features, labels=image_labels)

    return df
