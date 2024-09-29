FROM python:3.12-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /bin/uv

WORKDIR /app

COPY . .

# Creating virtual environment with dependencies from uv.lock
RUN uv sync --frozen

# Activating the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Expose the FastAPI application port
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]