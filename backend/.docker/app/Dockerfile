FROM python:3.12

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app/.venv/lib/python3.12/site-packages:$PYTHONPATH"

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ./backend/pyproject.toml ./backend/poetry.lock /app/

RUN poetry config virtualenvs.in-project true

RUN poetry install
