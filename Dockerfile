# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock /app/
COPY project /app/project
COPY conf /app/

RUN ls /app/project

# Install dependencies
RUN poetry install --no-dev

# Copy the rest of the code
COPY . /app

# Copy Flyte configuration file
COPY config.yaml /root/.flyte/config.yaml

# Set environment variable for Flyte configuration
ENV FLYTECTL_CONFIG=/root/.flyte/config.yaml

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the workflow when the container launches
CMD ["poetry", "run", "python", "project/workflows.py"]
