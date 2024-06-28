# OI.AI.DataEng.TakeHome

Python project to create a data pipeline (using airflow framework) to extract and resize frames from videos to generate image datasets for
video classification. These datasets will be used to train models for identifying marine animals in videos.

## Setup

In order to install and run the project there are 2 ways to do that. By one hand you can run locally and generate the dataset and by other hand you can run through a docker container.

### Setup Locally

To install and run the project locally, ensure you have Poetry and Python (version 3.8 or lower) installed, then follow these steps:

1. Install Poetry:

```bash
 pip install poetry
```

2. Create the environment:

```bash
poetry shell
poetry lock
poetry install
```

3. Add environment variable
```bash
export MAIN_SETTINGS='conf/settings.json'
```

4. Configure settings:

The conf folder contains the settings files for the project and tests. To change parameters for dataset generation, modify the values in settings.json:
```json
{
	"Video": {
		"output_folder": "dataset", #Dataset Output folder
		"extract_output_folder": "frames", #Inside the output folder you will have the video frames
		"resize_output_folder": "resize_frames", #Inside the output folder you will have the rezise frames
		"frame_rate": 10 #Value of frame rate
	}
}
```

5. Generate Dataset
```python
ve = VideoExtract()
ve.generate_image_dataset(video_path="5548408-uhd_3840_2160_25fps.mp4", size=(224, 224))
```

### Setup Docker

To be write


## Changes
When you need to change the code please follow the following steps:

1. Create a new branch
```bash
git checkout -b feature/<branch_name>
```

2. Make all the necessary changes
3. Add unit and integration tests to cover as much as possible the code implemented

```bash
export MAIN_SETTINGS='conf/settings.tests.json'
pytest --cov=project
```

4. Run all the lint commands
```bash
black project
isort project
```

5. Commit and push

When you push commits to this repository, a pre-commit hook will be triggered to ensure code quality and consistency. This hook will validate the following:

- **trailing-whitespace**: Ensures that there are no trailing whitespaces in your code.
- **end-of-file-fixer**: Ensures that the end of each file has exactly one newline.
- **check-yaml**: Validates that YAML files are properly formatted.
- **check-merge-conflict**: Checks for unresolved merge conflicts in the code.
