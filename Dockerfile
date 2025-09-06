FROM python:3.12-alpine

RUN apk add --update --no-cache bash

RUN mkdir /qortex

WORKDIR /qortex

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PATH=/usr/local/bin:$PATH

CMD python manage.py runserver 0.0.0.0:8000