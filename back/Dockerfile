FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY uv.lock pyproject.toml /app/

RUN uv sync

COPY . /app/

CMD ["uv", "run", "python", "manage.py", "runserver"]