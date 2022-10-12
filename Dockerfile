# FROM python:3.10
#
# RUN pip install poetry==1.2.0
# RUN pip install uvicorn
#
# COPY ./pyproject.toml ./poetry.lock* ./
#
# RUN poetry install --no-root --no-dev
# RUN poetry config virtualenvs.create false
#
# COPY ./app /app
#
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "localhost", "--port", "8000"]

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

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]