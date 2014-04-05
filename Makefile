run:
	@echo "run test webserver"
	sh start.sh

test:
	@echo "run test suit"
	py.test

setup:
	@echo "install default packages"
	pip install -r requirements.txt

setup-dev: setup
	@echo "install packages to developer"
	pip install -r requirements-dev.txt

clean:
	@echo "remove pyc files"
	find . -name "*.pyc" -delete

help:
	@echo "  run        run test webserver"
	@echo "  test       run test suit"
	@echo "  setup      install default packages"
	@echo "  setup-dev  install packages to developer"
	@echo "  clean      remove pyc files"
