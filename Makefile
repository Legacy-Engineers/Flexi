.PHONY: migrations migrate run clean test default

default:
	./dev_launch.sh

migrations:
	. .venv/bin/activate && python manage.py makemigrations

migrate:
	. .venv/bin/activate && python manage.py migrate

run:
	. .venv/bin/activate && python manage.py runserver

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

test:
	. .venv/bin/activate && python manage.py test


