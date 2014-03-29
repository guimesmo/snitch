run:
	python webserver.py

test:
	py.test

setup:
	pip install -r requirements.txt

clean:
	find . -name "*.pyc" -delete
