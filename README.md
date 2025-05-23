# python_template
Just another opinionated cookiecutter template to stop writing Python boilerplate and improve productivity

![example workflow](https://github.com/jazumaquero/python-template/actions/workflows/push-yaml/badge.svg)

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
This template is based on [cookiecutter](https://github.com/cookiecutter/cookiecutter), specially with version +1.7.
You can install with *pip*:

    pip install cookiecutter>=1.7

However, it's strongly recommended using *pipx* when it is available on your system:

    pipx install cookiecutter>=1.7

This repo is organized [cookiecutters in directories](https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html)
in order to simplify the maintenance of different use case and make it neater and fast dialog.

You can use following examples to build your projects from this template using following commands:

    # Create some python library/CLI project (use this as default
    cookiecutter https://github.com/jazumaquero/python_template.git --directory="library"

    # Create some python CLI project, mainly used for standalone applications won't require proper distribution
    cookiecutter https://github.com/jazumaquero/python_template.git --directory="cli"

    # Create some python application will run inside a Docker container. 
    cookiecutter https://github.com/jazumaquero/python_template.git --directory="docker"

## Features
* Python virtualenv creation, Packaging and Dependency management with [uv](https://docs.astral.sh/uv/). It is using latest standards, and it 
is much faster than *poetry* installing dependencies. Also allows skipping *pyenv* installation for getting some specific
python version.
* Virtualenv inside project directory is created (and named as ```.venv```), and *uv* will use as default virtual
environment, what maybe convenient in case you are using some IDE like *Pycharm* or *VisualStudioCode* (see config at
```poetry.toml``` file).
* Test framework is [pytest](https://docs.pytest.org/en/reorganize-docs/contents.html).
>* Examples given on docstring will be checked with [xdoctest](https://xdoctest.readthedocs.io/en/latest/autoapi/xdoctest/index.html).
* Coverage analysis is done with [coverage](https://coverage.readthedocs.io/en/stable/index.html).
* Reporting files created (currently for *pytest* and *coverage*) on inside project directory with name ```.reports```.
* Linting af formatting has been moving to [ruff](https://docs.astral.sh/ruff/), mainly due to it is extremely fast, and 
provides same features than a lot of additional packages. Also, it provides a way of defining all configuration inside
`pyproject.toml` file, reducing boilerplate. Deprecate the previous usage of:
>* [black](https://black.readthedocs.io/en/stable/index.html) . 
>* [isort](https://pycqa.github.io/isort/).
>* [flake8 framework](https://flake8.pycqa.org/en/latest/).
>* [pep8-naming](https://github.com/PyCQA/pep8-naming).
* Static Type checking using [mypy](https://mypy.readthedocs.io/en/latest/index.html).
* Runtime Type checking using [typeguard](https://typeguard.readthedocs.io/en/latest/index.html) with *pytest* integration.
* Generates documentation using [sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html).
>* Also allows using both *rst* and *md* files just by using [myst-parser](https://myst-parser.readthedocs.io/en/latest/).
>* Using *read-the-docs* template for rendering documentation.
* Continuous Integration using with [tox](https://tox.readthedocs.io/en/latest/), including
[tox-uv](https://github.com/tox-dev/tox-uv) integration (probably will include
[nox](https://nox.thea.codes/en/stable/) support later, but currently I use **Pycharm** a lot and its *tox* support is
quite convenient).
* Keep repository neater, just by using a bunch of useful [pre-commit hooks](https://pre-commit.com/) working together
with [ruff](https://docs.astral.sh/ruff/) to warranty standard coding conventions, and for keep imports in order.
* Allow generating changelog just by using [gitchangelog](https://github.com/vaab/gitchangelog).
* Allow using [click](https://palletsprojects.com/p/click/) to create CLI (command line interpreter) applications.
* Optionally create docker image with code (that may be useful when running web applications).
