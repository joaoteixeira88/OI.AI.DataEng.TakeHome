# Makefile

.PHONY: build up down run package register

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

run:
	docker-compose run flyte

package:
	poetry build
	tar -czvf package2.tar.gz project/create_dataset.py project/video_extract.py project/workflows.py project/crosscutting

register: package
	flytectl register files --project flytesnacks --domain development --archive package2.tar.gz
