import logging

import pytest

from project.video_extract import VideoExtract


class TestVideoExtract:
    def setup_method(self):
        self.ve = VideoExtract()

    def test_GenerateImageDataset_InvalidPathFile_RaiseValueError(self, caplog):
        # Act
        with caplog.at_level(logging.ERROR):
            with pytest.raises(ValueError) as e:
                self.ve.generate_image_dataset(video_path="aaaaa", size=(10, 10))

        # Assert
        assert "Something went wrong while reading the video." in caplog.text
