# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = docs/_build
DOCSDIR       = docs/

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(DOCSDIR)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(DOCSDIR)


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
	@echo
	find . -name "*.pyc" -delete

htmldocs:
	@echo "run sphinx docs"
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	open $(BUILDDIR)/html/index.html

epubdocs:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

help:
	@echo "  run        run test webserver"
	@echo "  test       run test suit"
	@echo "  setup      install default packages"
	@echo "  setup-dev  install packages to developer"
	@echo "  clean      remove pyc files"
	@echo "  htmldocs   create html sphinx docs"
	@echo "  epubdocs   create epub sphinx docs"
