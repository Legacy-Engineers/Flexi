.PHONY: migrations migrate run clean test default

default:
	./dev_launch.sh

migrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

run:
	uv run manage.py runserver

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

test:
	uv run manage.py test

install:
	uv sync
