FROM python:3.10-slim

WORKDIR /app

COPY src/ /app

RUN pip install click