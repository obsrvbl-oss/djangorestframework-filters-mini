NAME   := django-rest-framework-filters-mini
SOURCE := rest_framework_filters/
TESTS  := tests/
REQS   := requirements-dev.txt
PYEXE  := /usr/bin/python3.9

.PHONY: all env requirements test lint clean clean-cache clean-build

all: test lint

env: SHELL := /usr/bin/env fish
env:
	mkvirtualenv -p $(PYEXE) -a $(CURDIR) -r $(REQS) $(NAME)

requirements:
	pip install -U -r $(REQS)

oldtest: export DJANGO_SETTINGS_MODULE := tests.settings
oldtest:
	coverage run --source=$(SOURCE) --branch -m unittest -v; \
	coverage report --show-missing

test:
	coverage run --source=$(SOURCE) --branch manage.py test; \
	coverage report --show-missing

lint:
	pyflakes $(SOURCE) $(TESTS)
	black $(SOURCE) $(TESTS) -S --check

clean: clean-cache clean-build

clean-cache:
	rm -rf .mypy_cache/ .pytest_cache/ .hypothesis/ htmlcov/ .tox/
	rm -f .coverage
	find . -name '*.pyc' -type f -delete
	find . -name __pycache__ -type d -delete

clean-build:
	rm -rf *.egg-info/ build/ dist/
