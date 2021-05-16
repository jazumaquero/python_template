## Base python image
FROM python:{{ cookiecutter.python_version }}-stretch AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# Lets use following working directory
WORKDIR /app

## NOTE: remember including here any extra dependency you may want to install.

## Builder stage
FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.5

# To run build stage, is required to have poetry installed,
# and create some virtual environment where application will be store
RUN pip install "poetry==$POETRY_VERSION" && python -m venv /venv

# To install all dependencies into virtual environment, just copy poetry.lock file
# and the transform into some requirements format can be read by pip
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

# Then copy code and install any extra distribution wheel not already included.
COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

## Release stage
FROM base as release

# Get virtualenv from builder stage, so that, only really required dependencies will be installed
COPY --from=builder /venv /venv
# And the copy code (what may be useful when running some kind of application (i.e. web applications
COPY . .

# Run application with entry point
CMD ["./docker-entrypoint.sh"]