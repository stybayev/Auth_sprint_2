FROM --platform=linux/amd64 python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update -y
RUN apt-get install gcc -y
RUN pip install -r requirements.txt
COPY . /app

CMD uvicorn --reload --host=$RATING_REVIEW_SERVICE_UVICORN_HOST --port=$RATING_REVIEW_SERVICE_UVICORN_PORT rating_review_service.main:app
