all: install

configure:
	@poetry install

lint:
	@poetry run flake8
