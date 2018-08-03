pkg: setup.py src/*.py
	python3 -m pip install --user --upgrade setuptools wheel && \
	python3 setup.py sdist bdist_wheel

pip: dist/*
	python3 -m pip install --user --upgrade twine && \
	twine upload dist/*
