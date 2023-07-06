FROM python:3.11.2
LABEL authors="hdc"

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PORT_NUMBER 8501

# Define working directory
WORKDIR /app

# Update apt-get and install gcc
RUN apt-get update && apt-get install apt-utils && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# install pg_config
RUN apt-get update && apt-get install wget ca-certificates -y && apt-get install -y gnupg2
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt bullseye-pgdg main" > /etc/apt/sources.list.d/pgdg.list'&& apt-get update && apt-get install postgresql postgresql-contrib -y

# Install python dependencies in /.venv
#COPY Pipfile .
#COPY Pipfile.lock .
COPY requirments.txt .

# Install pipenv and compilation dependencies
#RUN pip install -U setuptools pip pipenv
#RUN pipenv install --system --deploy
RUN pip install -r requirments.txt

# Copy project on mac
#COPY .. .

# on linux machine access control do not allow copy outside path
COPY . .



# Rename .env.docker file to .env
RUN mv .env.dev .env

# Command to run when app starts
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]