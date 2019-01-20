# -- Development ----------------------#

.PHONY: install-dev
install-dev:
	pip install -e .[dev]

.PHONY: build-dist
build-dist: clean
	python setup.py sdist bdist_wheel

.PHONY: publish-dev
publish-dev: build-dist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: test
test:
	pytest test

.PHONY: tox
tox:
	tox


# -- Production -----------------------#

.PHONY: install
install:
	python setup.py install

.PHONY: publish-prod
publish-prod: build-dist
	twine upload dist/*


# -- Setup ----------------------------#

.PHONY: clean
clean:
	rm -rf dist/ build/ nb_py.egg* && \
	find . \( -name __pycache__ \
		-o -name "*.pyc" \
		-o -name .pytest_cache \
		-o -name .eggs \
		\) -exec rm -rf {} +\
