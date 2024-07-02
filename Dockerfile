FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN pip install poetry
RUN poetry install --no-root

COPY . /app

ENTRYPOINT ["python"]
CMD ["project/workflows.py"]
