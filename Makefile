release:
	pip install -r requirements.txt

dev: release
	pip install -r requirements-dev.txt

test: dev
	python -m unittest

lint: dev
	mypy ./phonenumber.py ./tests.py
	flake8
