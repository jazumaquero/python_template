import logging
import os
import subprocess
import sys

# Target Python version choose by user
REQUIRED_PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# Commands for installing UV
CHECK_UV_COMMAND = "uv --version"
INSTALL_UV_COMMAND_LINUX = "curl -LsSf https://astral.sh/uv/install.sh | sh"
INSTALL_UV_COMMAND_WINDOWS = 'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"'

# Command template to update UV to latest values
UPDATE_UV_COMMAND = "uv self update"

# Command template to install some specific Python version with uv
INSTALL_PYTHON_COMMAND = f"uv venv --python {REQUIRED_PYTHON_VERSION}"

# Command template to ensure tox and pre-commit are installed
INSTALL_PRE_COMMIT_AND_TOX_COMMAND = 'uv add "tox[tox-uv]>=4.25.0" pre-commit --dev'

# Command template to install all dependencies on virtual environment
INSTALL_DEPENDENCIES_ON_VIRTUAL_ENVIRONMENT_COMMAND = "uv sync --locked --all-extras --dev"

# Command template to initialize git with pre-commit hooks
INIT_GIT_ON_PROJECT_COMMAND = "git init && pre-commit install"


def install_base_dependencies():
    def ensure_uv_is_installed():
        logging.info("Ensure UV is installed")
        try:
            is_installed = (subprocess.run(CHECK_UV_COMMAND.split(), capture_output=True).returncode == 0)
        except:
            is_installed = False
        if not is_installed:
            logging.info("Installing UV")
            cmd = INSTALL_UV_COMMAND_WINDOWS if sys.platform.startswith("win") else INSTALL_UV_COMMAND_LINUX
            os.system(cmd)
        else:
            logging.info("UV is already installed")

    def ensure_uv_is_updated():
        logging.info("Ensure UV is updated")
        os.system(UPDATE_UV_COMMAND)

    def ensure_python_version_is_installed():
        logging.info(f"Following Python version will be installed: {REQUIRED_PYTHON_VERSION}")
        os.system(INSTALL_PYTHON_COMMAND)

    def ensure_pre_commit_and_tox_are_installed():
        logging.info("Installing pre-commit and tox.")
        os.system(INSTALL_PRE_COMMIT_AND_TOX_COMMAND)

    def install_all_dependencies():
        logging.info("Install all dependencies on virtual environment.")
        os.system(INSTALL_DEPENDENCIES_ON_VIRTUAL_ENVIRONMENT_COMMAND)

    def init_git_on_local():
        logging.info("Initialize git repository on local with pre-commit hooks.")
        os.system(INIT_GIT_ON_PROJECT_COMMAND)

    ensure_uv_is_installed()
    ensure_uv_is_updated()
    ensure_python_version_is_installed()
    ensure_pre_commit_and_tox_are_installed()
    install_all_dependencies()
    init_git_on_local()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    install_base_dependencies()
