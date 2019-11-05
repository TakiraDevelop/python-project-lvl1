all: install

configure:
	@poetry install

make: lint
	@poetry run flake8
