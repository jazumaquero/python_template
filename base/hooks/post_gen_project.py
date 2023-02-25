import logging
import os
import sys

# Target Python version choose by user
REQUIRED_PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# Command template to update pyenv to latest values
UPDATE_PYENV_COMMAND = "pyenv update"

# Command template to find latest available Python version from pyenv given required version (BASH required)
FIND_LATEST_PYTHON_VERSION_AVAILABLE_COMMAND = "pyenv install --list | grep -v - | grep -v b | grep {} | tail -1"

# Command template to install some specific Python version with pyenv
INSTALL_PYTHON_COMMAND = "pyenv install {}"

# Command template to ensure poetry, tox and pre-commit are installed
INSTALL_POETRY_AND_TOX_COMMAND = "pyenv local {} && pip install --upgrade pip && pipx install poetry && pipx install tox && pipx install pre-commit"

# Command template to create some virtual environment inside project folder (make easy to use IDEs)
CREATE_VIRTUAL_ENVIRONMENT_COMMAND = "pyenv local {} && python -m venv .venv"

# Command template to install all dependencies on virtual environment
INSTALL_DEPENDENCIES_ON_VIRTUAL_ENVIRONMENT_COMMAND = "poetry install"

# Command template to initialize git with pre-commit hooks
INIT_GIT_ON_PROJECT_COMMAND = "git init && pre-commit install"


def install_base_dependencies():
    def get_latest_python_version():
        if sys.platform.startswith("win"):
            sys.exit("Windows platform currently not supported")
        else:
            cmd = FIND_LATEST_PYTHON_VERSION_AVAILABLE_COMMAND.format(REQUIRED_PYTHON_VERSION)
            latest_version = os.popen(cmd).read().strip()
            logging.info("Using more recent python version from {}: {}".format(REQUIRED_PYTHON_VERSION, latest_version))
            return latest_version

    def ensure_pyenv_is_updated():
        logging.info("Updating pyenv")
        os.system(UPDATE_PYENV_COMMAND)

    def ensure_python_version_is_installed():
        logging.info("Following Python version will be installed: {}".format(python_version))
        cmd = INSTALL_PYTHON_COMMAND.format(python_version)
        os.system(cmd)

    def ensure_poetry_and_tox_are_installed():
        logging.info("Installing poetry.")
        cmd = INSTALL_POETRY_AND_TOX_COMMAND.format(python_version)
        os.system(cmd)

    def ensure_virtual_env_is_created():
        logging.info("Creating virtualenv inside project directory.")
        cmd = CREATE_VIRTUAL_ENVIRONMENT_COMMAND.format(python_version)
        os.system(cmd)

    def install_all_dependencies():
        logging.info("Install all dependencies on virtual environment.")
        cmd = INSTALL_DEPENDENCIES_ON_VIRTUAL_ENVIRONMENT_COMMAND
        os.system(cmd)

    def init_git_on_local():
        logging.info("Initialize git repository on local with pre-commit hooks.")
        cmd = INIT_GIT_ON_PROJECT_COMMAND
        os.system(cmd)

    ensure_pyenv_is_updated()
    python_version = get_latest_python_version()
    ensure_python_version_is_installed()
    ensure_poetry_and_tox_are_installed()
    ensure_virtual_env_is_created()
    install_all_dependencies()
    init_git_on_local()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    install_base_dependencies()
