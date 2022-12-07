# syntax=docker/dockerfile:1
#FROM python:3.11-alpine
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /GasCan
COPY requirements.txt /GasCan/
RUN pip install -r requirements.txt
COPY . /GasCan/