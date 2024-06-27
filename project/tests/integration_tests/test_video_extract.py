import os
import shutil

from project.crosscutting.configs import Config
from project.video_extract import VideoExtract


class TestVideoExtract:
    def setup_method(self):
        self.test_path = 'project/tests'
        self.dataset_path = f'{Config.Video.output_folder}'
        self.resize_output_folder = Config.Video.resize_output_folder
        self.ve = VideoExtract()

    def teardown_method(self):
        shutil.rmtree('project/tests/dataset')

    def test_GenerateImageDataset_ValidInput_ShouldHaveTheDatasetWith5Elements(self):
        # Act
        self.ve.generate_image_dataset(
            video_path=f'{self.test_path}/integration_tests/data/test_video.mp4',
            size=(10, 10),
        )

        # Assert
        assert os.path.exists(f'{self.dataset_path}')
        assert os.path.exists(f'{self.dataset_path}/{self.resize_output_folder}')
        assert (
            len(
                [
                    name
                    for name in os.listdir(
                        f'{self.dataset_path}/{self.resize_output_folder}'
                    )
                    if name.endswith('.jpg')
                ]
            )
            == 5
        )
