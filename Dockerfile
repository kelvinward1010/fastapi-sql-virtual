FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY pyproject.toml poetry.lock /src/

RUN apt-get update && apt-get install -y \ 
    libpq-dev gcc \ 
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

RUN poetry install --no-root

COPY . /src/

RUN poetry run alembic upgrade head

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
