# Variables
IMAGE_NAME = flyte-video-classification

# Docker build command
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Ensure data directory exists
.PHONY: prepare
prepare:
	mkdir -p data/output

# Docker run command
.PHONY: run
run: prepare
	docker run -it --rm -v $(PWD)/data:/app/data $(IMAGE_NAME)

# Flytekit run command (adjust the paths as necessary)
.PHONY: flyte-run
flyte-run:
	docker run -it --rm -v $(PWD)/data:/app/data $(IMAGE_NAME) poetry run pyflyte run --remote \
	--project project --domain development \
	project/workflows.py video_to_images_workflow \
	--video_path data/sample_video.mp4 --resize_width 224 --resize_height 224 --frame_rate 10

#docker run -it --rm -v data:/app/data flyte-video-classification poetry run pyflyte run --remote --project project --domain development project/workflows.py video_to_images_workflow --video_path 5548408-uhd_3840_2160_25fps.mp4

# Clean the output directory
.PHONY: clean
clean:
	rm -rf data/output
