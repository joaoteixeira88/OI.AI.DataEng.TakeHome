import logging
import os

import pytest

from project.video_extract import extract_frames, resize_frames


class TestVideoExtract:
    def test_ExtractFrames_InvalidPathFile_RaiseValueError(self, caplog):
        # Act
        with caplog.at_level(logging.ERROR):
            with pytest.raises(ValueError) as e:
                extract_frames(
                    video_path="aaaaa",
                    extract_output_folder="out_folder",
                    frame_rate=10,
                )

        # Assert
        assert "Something went wrong while reading the video." in caplog.text

    def test_ResizeFrames_ExtractFolderNotExists_RaiseFileNotFoundError(self, caplog):
        # Act
        with caplog.at_level(logging.ERROR):
            with pytest.raises(FileNotFoundError) as e:
                resize_frames(
                    resize_width=10,
                    resize_height=10,
                    resize_output_folder="out_folder",
                    extract_output_folder="extract_folder",
                )

        # Assert
        assert "Extract output folder extract_folder does not exist." in caplog.text

    def test_ResizeFrames_FolderWithoutExtractedFrames_OutputFolderEmpty(self):
        # Arrange
        os.mkdir("extract_folder")

        # Act
        resize_frames(
            resize_width=10,
            resize_height=10,
            resize_output_folder="out_folder",
            extract_output_folder="extract_folder",
        )

        # Assert
        assert len([name for name in os.listdir("out_folder")]) == 0

        os.rmdir("extract_folder")
        os.rmdir("out_folder")
