import os

from cookiecutter.main import cookiecutter
from pytest import mark

CURRENT_PATH = os.path.dirname(__file__)
BASE_DIRECTORY = os.path.join(CURRENT_PATH, "../")
OUTPUT_DIRECTORY = os.path.join(BASE_DIRECTORY, ".target")
RESOURCES_DIRECTORY = os.path.join(CURRENT_PATH, "resources")


@mark.parametrize(
    "directory,config_file",
    [
        ("cli", "cli_config.yaml"),
        ("library", "library_config.yaml"),
        ("docker", "docker_config.yaml"),
    ],
)
def test_template_generation(directory: str, config_file: str):
    # Lets start with naive approach that just verify template syntax is fine
    cookiecutter(
        template=BASE_DIRECTORY,
        directory=os.path.join(BASE_DIRECTORY, directory),
        config_file=os.path.join(RESOURCES_DIRECTORY, config_file),
        no_input=True,
        overwrite_if_exists=True,
        output_dir=OUTPUT_DIRECTORY,
    )
