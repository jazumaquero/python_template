# python_template
Just another opinionated cookiecutter template to stop writing Python boilerplate and improve productivity

## Introduction
Main objective of this template is to explore modern Python tools that may help on your daily basis job, mainly focus on
any activity related with Continuous Integration (CI) and Continuous Delivery (CD), what may become quite handy when you
want to start some new project

## Inspiration
This template is inspired on awesome work previously made by [Claudio Jolowicz](https://github.com/cjolowicz/) at
[Hypermodern Python template](https://github.com/cjolowicz/cookiecutter-hypermodern-python) and on excellent article
from [Cristobal Carnero Liñán](https://github.com/cristobalcl) 
[How to start a Python project with Django in 2020](https://medium.com/@cristobalcl/how-to-start-a-python-project-with-django-in-2020-803122721b23).

Anyway, you won't find any kind of silver bullets or golden hammers out there, so that, I have adapted their excellent
work to my own way of working and my personal preferences, so, this template probably won't meet your expectations,
because, as I have already mentioned, is some *opinionated template*.

So, please explore solutions already available out there, understand them, and adapt to your own way of working. In
other words,*do not re-invent the wheel!*.

## Requirements
### Python
You must have installed any kind of Python version on your system. Don't worry about the Python version mismatch with
Python version you want to use for development, because [pyenv](https://github.com/pyenv/pyenv) will be used later to
obtain desired version.

In case of most of Linux base operative systems some Python version is already installed.

### Cookiecutter
This template is based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), and you can install with *pip*:

    pip install cookiecutter

However, it's strongly recommended using *pipx* when it is available on your system:

    pipx install cookiecutter

### Pyenv
As mentioned before, this cookiecutter template will use *pyenv* to install specific Python version you want to use for
development (this template is focused on using a single Python version).

In case of Linux base system, it is recommended using [pyenv-installer](https://github.com/pyenv/pyenv-installer):

    curl https://pyenv.run | bash

In case of using windows, you can use [pyenv-win](https://github.com/pyenv-win/pyenv-win)

## Features
* Ensure required Python version is already installed with [pyenv](https://github.com/pyenv/pyenv). 
* Packaging and Dependency management with [poetry](https://python-poetry.org/).
* Virtualenv inside project directory is created (and named as ```.venv```), and *poetry* will use as default virtual
environment, what maybe convenient in case you are using some IDE like *Pycharm* or *VisualStudioCode* (see config at
```poetry.toml``` file).
* Test framework is [pytest](https://docs.pytest.org/en/reorganize-docs/contents.html).
>* Examples given on docstring will be checked with [xdoctest](https://xdoctest.readthedocs.io/en/latest/autoapi/xdoctest/index.html).
* Coverage analysis is done with [coverage](https://coverage.readthedocs.io/en/stable/index.html).
* Reporting files created (currently for *pytest* and *coverage*) on inside project directory with name ```.reports```.
* Linting is made with [flake8 framework](https://flake8.pycqa.org/en/latest/), including:
>* Proper naming convention check with [pep8-naming](https://github.com/PyCQA/pep8-naming).
>* Added [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear) to early detect bug and risky designs.
>* Added [flake8-bandit](https://github.com/tylerwince/flake8-bandit) to include some more extra rules.
>* Added [flake8-docstrins](https://gitlab.com/pycqa/flake8-docstrings) and
[flake8-rst-docstrings](https://github.com/peterjc/flake8-rst-docstrings) for **docstring** linting.
>* Also added [darglint](https://github.com/terrencepreilly/darglint) as **flake8** plugin to lint documentation.
>* Configuration included at ```.flake8``` file.
* Static Type checking using [mypy](https://mypy.readthedocs.io/en/latest/index.html).
* Runtime Type checking using [typeguard](https://typeguard.readthedocs.io/en/latest/index.html) with *pytest* integration.
* Generates documentation using [sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html).
>* Also allows using both *rst* and *md* files just by using [myst-parser](https://myst-parser.readthedocs.io/en/latest/).
>* Using *read-the-doscs* template for rendering documentation.
* Continuous Integration using with [tox](https://tox.readthedocs.io/en/latest/), including
[tox-poetry](https://github.com/tkukushkin/tox-poetry) integration (probably will include
[nox](https://nox.thea.codes/en/stable/) support later, but currently I use **Pycharm** a lot and its *tox* support is
quite convenient).
* Keep repository neater, just by using a bunch of useful [pre-commit hooks](https://pre-commit.com/) working together
with [black](https://black.readthedocs.io/en/stable/index.html) to warranty standard coding conventions,
and [isort](https://pycqa.github.io/isort/) for keep imports in order.
* Allow generating changelog just by using [gitchangelog](https://github.com/vaab/gitchangelog).
* Allow using [click](https://palletsprojects.com/p/click/) to create CLI (command line interpreter) applications.
