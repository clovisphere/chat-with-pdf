FROM python:3.11-slim
LABEL authors="clov"

ENV CONTAINER_HOME=/var/www/chat-with-pdf
ENV PORT_NUMBER=8501

# update apt-get and install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set work directory
WORKDIR $CONTAINER_HOME
# upgrade pip, install pipenv and importlib_metadata
RUN pip install --upgrade pip pipenv
# install dependencies
COPY ../Pipfile* .
RUN pipenv install --system --deploy --ignore-pipfile
# copy project
COPY ../.. .
# Rename .env.docker file to .env
RUN mv .env.dev .env
# Command to run when app starts
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=$PORT_NUMBER", "--server.address=0.0.0.0"]