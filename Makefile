run:
	sh start.sh

test:
	py.test

setup:
	pip install -r requirements.txt

clean:
	find . -name "*.pyc" -delete
