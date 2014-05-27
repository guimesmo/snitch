Starting to developer
=====================

**Read the documentation before start to write code.**

Sandbox
-------

Work with virtualenv is a good idea to protect your packages
and organize your work.

Read more about virtualenv_

.. _virtualenv : http://www.virtualenv.org/en/latest/

Can I help you ?
----------------

Read issues or create issues on Github.
Remeber to search about your doubts before write one new issue.

Read one issue GitHubIssues_

.. _GitHubIssues : https://github.com/nsndev/snitch/issues

Setup you project
-----------------

Do you know Makefile ?

Makefile_ options:
    **run:**
        sh start.sh
    **test:**
        py.test
    **setup:**
        pip install -r requirements.txt
    **setup-dev**: setup
        pip install -r requirements-dev.txt
    **clean:**
        find . -name "*.pyc" -delete

To install all packages necessary to developer use command **make setup-dev**

.. _Makefile : http://mrbook.org/tutorials/make/
