import logging
import os

import cv2

from project.crosscutting.configs import Config
from project.crosscutting.utils import create_folder


class VideoExtract:
    """
    This class make some data process regarding video
    images in order to have datasets used to train
    models for identifying marine animals in videos.
    """

    def __init__(self):
        self.frame_rate = Config.Video.frame_rate
        self.output_folder = Config.Video.output_folder
        self.extract_output_folder = f"{self.output_folder}/{Config.Video.extract_output_folder}"
        self.resize_output_folder = f"{self.output_folder}/{Config.Video.resize_output_folder}"

    def generate_image_dataset(self, video_path: str, size: (int, int)) -> None:
        """
            Generate an image dataset by extracting and resizing frames from a video.

        Args:
        ----
            video_path (str): Video path to generate the dataset.
            size (tuple): Desired size of the output images (width, height). Default is (224, 224).
        """

        logging.info("Generate Image Dataset")

        self.__extract_frames(video_path)
        self.__resize_frames(size)

        logging.info(f"Dataset generated in {self.resize_output_folder}")

    def __extract_frames(self, video_path: str) -> None:
        """Extract the video frames taking in consideration
        the frame rate and save the multiples images on an
        output folder.

        Args:
        ----
            output_folder (str): Output folder of the extracted frames.
            frame_rate (int): Frame rate to extract the images from video.
        """

        logging.info("Extracting video frames")
        create_folder(self.extract_output_folder)
        cap = cv2.VideoCapture(video_path)

        count = 0
        success, image = cap.read()

        if not success:
            logging.error("Something went wrong while reading the video.")
            raise ValueError

        while success:
            if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % self.frame_rate == 0:
                cv2.imwrite(
                    os.path.join(self.extract_output_folder, f"frame{count:06d}.jpg"),
                    image,
                )
                count += 1
            success, image = cap.read()
        cap.release()

    def __resize_frames(self, size: (int, int)):
        """
        Resize extracted frames to the desired size.

        Args:
        ----
            size (int, int): width and height to resize the images.
            frame_rate (int): Frame rate to extract the images from video.
        """

        logging.info("Extracting video frames")
        create_folder(self.resize_output_folder)

        for filename in os.listdir(self.extract_output_folder):
            if filename.endswith(".jpg"):
                img = cv2.imread(os.path.join(self.extract_output_folder, filename))
                img_resized = cv2.resize(img, size)
                cv2.imwrite(
                    os.path.join(self.resize_output_folder, filename), img_resized
                )


#ve = VideoExtract()
#ve.generate_image_dataset(video_path="5548408-uhd_3840_2160_25fps.mp4", size=(224, 224))