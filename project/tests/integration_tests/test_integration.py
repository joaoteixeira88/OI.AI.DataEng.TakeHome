import os
import shutil

import pandas as pd

from project.workflows import video_to_images_workflow


class TestIntegration:
    def setup_method(self):
        self.test_path = "project/tests"

    def teardown_method(self):
        shutil.rmtree("dataset")

    def test_GenerateImageDataset_ValidInput_ShouldHaveTheDatasetWith5Elements(self):
        # Act
        result = video_to_images_workflow(
            video_path=f"{self.test_path}/integration_tests/data/test_video.mp4",
            resize_width=10,
            resize_height=10,
            frame_rate=50,
        )

        # Assert
        assert os.path.exists("dataset")
        assert os.path.exists("dataset/frames")
        assert (
            len(
                [name for name in os.listdir("dataset/frames") if name.endswith(".jpg")]
            )
            == 5
        )

        assert isinstance(result, pd.DataFrame)
        assert len(result) == 5
        assert len(result.columns) == 4
