FROM python:3.9-buster

RUN mkdir app
Workdir /app

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml .
RUN poetry install
