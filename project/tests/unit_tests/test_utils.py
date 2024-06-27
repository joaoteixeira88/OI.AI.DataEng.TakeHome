import logging
import os

import pytest

from project.crosscutting.utils import create_folder


class TestUtils:
    def test_CreateFolder_ValidParameterWhereFolderNotExists_FolderShouldBeCreated(
        self,
    ):
        # Arrange
        folder_name = "test_folder"

        # Act
        create_folder(folder_name)

        # Assert
        assert os.path.exists(folder_name)

        os.removedirs(folder_name)

    def test_CreateFolder_InvalidParameter_RaiseTypeErrorException(self, caplog):
        # Act
        with caplog.at_level(logging.ERROR):
            with pytest.raises(TypeError) as e:
                create_folder(folder_name="")

        # Assert
        assert "The folder name must be passed as an argument" in caplog.text
