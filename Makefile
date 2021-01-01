install:
	poetry install

call_stats:
	poetry run call_stats

lint:
	poetry run flake8 call_stats

build:
	poetry build

package-install:
	python3.8 -m pip install --user dist/*.whl

test:
	poetry run pytest tests/

.PHONY: install call_stats lint build package-install test

