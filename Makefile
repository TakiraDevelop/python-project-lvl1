all: install

configure:
	@poetry install

make:
	@poetry run flake8
