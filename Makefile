.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv;
	pip install -r requirements.txt;

db:
	python manage.py db init
	python manage.py db migrate -m "initial commit"
	python manage.py db upgrade

tests:
	python manage.py test

run:
	python manage.py run

all: clean install db tests run



migrate:
	python manage.py db migrate
	python manage.py db upgrade