.PHONY: build start stop clean

build:
	docker-compose build --no-cache

start:
	docker-compose up --force-recreate

stop:
	docker-compose down

clean:
	docker-compose down --volumes --rmi all --remove-orphans
