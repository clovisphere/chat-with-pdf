FROM python:3.11.2-slim
LABEL authors="clov"

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PORT_NUMBER 8501

# Define working directory
WORKDIR /app

# Update apt-get and install gcc
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Install python dependencies in /.venv
#COPY Pipfile .
#COPY Pipfile.lock .
COPY requirments.txt .

# Install pipenv and compilation dependencies
RUN #pip install -U setuptools pip pipenv
RUN #pipenv install --system --deploy
RUN pip install -r requirments.txt

# Copy project
COPY .. .

# Rename .env.docker file to .env
RUN mv .env.dev .env

# Command to run when app starts
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=$PORT_NUMBER", "--server.address=0.0.0.0"]