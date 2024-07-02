# OI.AI.DataEng.TakeHome

Python project to create a data pipeline (using flyte framework) to extract and resize frames from videos to generate image datasets for
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

5. Generate Dataset
The are two ways of executing that, by code or using the pyflyte.

Incorporated in the code:

```python
from project.workflows import video_to_images_workflow

video_to_images_workflow(video_path="5548408-uhd_3840_2160_25fps.mp4", resize_width=224, resize_height=224, frame_rate=10)
```

Trough command line using pyflyte:
```bash
pyflyte run --project project --domain development project/workflows.py video_to_images_workflow --video_path 5548408-uhd_3840_2160_25fps.mp4 --resize_width 224 --resize_height 224 --frame_rate 10
```


### Setup Docker/Kubernetes ( ⚠️ Is not currently working  )

Is not currently working the dockerization of the project and of flytectl.


## Changing Code Steps
When you need to change the code please follow the following steps:

1. Create a new branch
```bash
git checkout -b feature/<branch_name>
```

2. Make all the necessary changes
3. Add unit and integration tests to cover as much as possible the code implemented

```bash
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

## Developments

* [x] Use a workflow orchestration tool to build the data pipeline: Flyte.
* [x] Parameterize the number of frames-per-second to extract and the resolution of the generated images.
* [x] Provide clear and concise documentation on how to set up and run the service.
* [x] Use pre-commit hooks and lint the code.
* [x] Add automated tests and perform data validation.
* [ ] Deploy the service in Kubernetes. - All the configurations are almost done but is retrieving an error when executing the command `make register`
* [x] Create a public or private repository and name it OI.AI.DataEng.TakeHome.
* [x] Ensure the repository includes a comprehensive README file with setup instructions.
