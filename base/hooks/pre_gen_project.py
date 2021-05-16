import re
import sys

# Input arguments coming from cookiecutter prompt
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PACKAGE_NAME = "{{ cookiecutter.package_name }}"
DESCRIPTION = "{{ cookiecutter.description }}"
AUTHOR = "{{ cookiecutter.author }}"
EMAIL = "{{ cookiecutter.email }}"

# Regular expression that can identify if a string is a valid email address
VALID_EMAIL_REGEX = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

# Regular expression that can identify if a string is in snake_case style
IS_SNAKE_CASE_REGEX = r"^[a-z]+(\_{1}[a-z]+)*$"

# Regular expression that can identify if a string is in kebab-case style
IS_KEBAB_CASE_REGEX = r"^[a-z]+(\-{1}[a-z]+)*$"


def is_valid_project_name():
    if not re.search(IS_KEBAB_CASE_REGEX, PROJECT_NAME):
        return False, "Project name is required and must be non empty string in kebab-case format."
    else:
        return True, None


def is_valid_package_name():
    if not re.search(IS_SNAKE_CASE_REGEX, PACKAGE_NAME):
        return False, "Package name is required and must be non empty string in snake_case format."
    else:
        return True, None


def is_valid_description():
    if not DESCRIPTION:
        return False, "Description is required and must be non empty string."
    else:
        return True, None


def is_valid_author():
    if not AUTHOR:
        return False, "Author name is required and must be non empty string."
    else:
        return True, None


def is_valid_email():
    if not re.search(VALID_EMAIL_REGEX, EMAIL):
        return False, "Email address is required and must have valid syntax."
    else:
        return True, None


def validate_template_arguments():
    validations = [is_valid_project_name, is_valid_package_name, is_valid_description, is_valid_author, is_valid_email]
    errors = [message for is_valid, message in [validation() for validation in validations] if not is_valid]
    if errors:
        validation_message = "\n".join(["- {}".format(error) for error in errors])
        sys.exit("Project creation stopped due to validation errors were found: \n{}".format(validation_message))


if __name__ == "__main__":
    validate_template_arguments()
