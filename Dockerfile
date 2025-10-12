FROM python:3.12-slim AS build
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app

COPY requirements.txt .
COPY techronomicon /app
COPY techronomicon/entrypoint.py /app/entrypoint.py

RUN pip install -r requirements.txt && \
    chmod +x /app/entrypoint.py && \
    mkdir -p /app/media

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN useradd -u 999 -r -s /usr/sbin/nologin appuser && \
    mkdir -p /app && \
    chown -R 999:999 /app

COPY --from=build /usr/local /usr/local
COPY --from=build /app /app

ENV DJANGO_SETTINGS_MODULE=techronomicon.settings
USER 999:999
EXPOSE 8000
CMD ["/app/entrypoint.py"]