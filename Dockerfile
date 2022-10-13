FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock* /code

RUN pip install --upgrade pip
RUN pip install poetry==1.2.0

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY /app /code/app/
