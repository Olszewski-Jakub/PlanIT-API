.ONESHELL:

.PHONY: clean install tests run all

install:
	virtualenv venv;
	pip install -r requirements.txt;

db:
	python3 manage.py db init
	python3 manage.py db migrate -m "initial commit"
	python3 manage.py db upgrade	

tests:
	python manage.py test

clean:
	python3 -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
	python3 -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"

run:
	python3 manage.py run
	

all: clean install db tests run


migrate:
	python3 manage.py db migrate
	python3 manage.py db upgrade