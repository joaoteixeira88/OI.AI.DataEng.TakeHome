from typing import List, Sequence

import numpy as np

from project.create_dataset import create_dataframe, extract_features


class TestCreateDataset:
    def test_ExtractFeatures_EmptyInput_EmptyList(self):
        # Arrange
        image_data = np.empty(0)

        # Act
        result = extract_features(image_data=image_data)

        # Assert
        assert result == []

    def test_ExtractFeatures_ValidInput_ValidFeatures(self):
        # Arrange
        image_data = np.full((5, 3), 10)
        expected_result = [
            (10.0, 0.0, 0.0),
            (10.0, 0.0, 0.0),
            (10.0, 0.0, 0.0),
            (10.0, 0.0, 0.0),
            (10.0, 0.0, 0.0),
        ]

        # Act
        result = extract_features(image_data=image_data)

        # Assert
        assert result == expected_result
