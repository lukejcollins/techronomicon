[![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?logo=django&logoColor=white&labelColor=092E20&color=white)](https://www.djangoproject.com/) [![Docker](https://img.shields.io/badge/Docker-Containerisation-2496ED?logo=docker&logoColor=white&labelColor=2496ED&color=white)](https://www.docker.com/) ![Build](https://github.com/lukejcollins/techronomicon/actions/workflows/deploy.yml/badge.svg)

# Techronomicon

A small Django-powered blog. This repository contains the Django project, a blog app, and a container build that runs the site with Gunicorn and WhiteNoise.

This README focuses on the application and the image build process in isolation (no external orchestration).

## Overview

- Framework: Django 4.x
- App: `techronomiblog` (posts and about page)
- WSGI: Gunicorn
- Static files: WhiteNoise (`collectstatic` runs at container start)
- Database: PostgreSQL (via `psycopg`)
- Health check: `GET /healthz` returns `ok`

Project layout:

- `techronomicon/` – Django project and blog app
- `Dockerfile` – multi-stage Python 3.12 image
- `requirements.txt` – Python dependencies
- `.env` – local development environment variables
- `.env.docker` – container-friendly environment variables

## Environment variables

The application is configured via environment variables (and can optionally load `.env` when `LOAD_DOTENV=true`). Required variables:

- `SECRET_KEY` – Django secret key
- `DEBUG` – `true|false`
- `HOST` – logical host name for the app
- `ALLOWED_HOSTS` – comma-separated hostnames (e.g. `localhost,127.0.0.1`)
- `CSRF_TRUSTED_ORIGINS` – comma-separated origins (e.g. `http://localhost,http://127.0.0.1`)
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` – PostgreSQL settings
- `LOAD_DOTENV` – set to `true` to read `.env` (optional)

See `.env` and `.env.docker` for working examples.

## Local development (without Docker)

Prerequisites: Python 3.12+, PostgreSQL

1) Create and activate a virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```
pip install -r requirements.txt
```

3) Configure environment

Set variables from `.env` (or export them in your shell). Ensure PostgreSQL is available and the database exists.

4) Run migrations and start the dev server

```
python techronomicon/manage.py migrate
python techronomicon/manage.py runserver 0.0.0.0:8000
```

Visit `http://localhost:8000` and `http://localhost:8000/healthz`.

## Docker build and run

Build the image:

```
docker build -t techronomicon:dev .
```

Run database migrations (one-off) using the image:

```
docker run --rm \
  --env-file .env.docker \
  --entrypoint python \
  techronomicon:dev techronomicon/manage.py migrate
```

Run the application:

```
docker run --rm -p 8000:8000 \
  --env-file .env.docker \
  techronomicon:dev
```

Notes

- The container executes `/app/entrypoint.py`, which runs `collectstatic` and starts Gunicorn on port 8000.
- Ensure the PostgreSQL instance referenced by `.env.docker` is reachable (e.g. `DB_HOST=host.docker.internal` on macOS/Windows).

## Continuous integration (build only)

GitHub Actions builds the Docker image from the repository and can push it to GitHub Container Registry (GHCR). The workflow lives under `.github/workflows/` and the badge above reflects its status.

Typical tags to publish include a commit-SHA tag and `latest` for the default branch.

## Contributing

Issues and PRs are welcome. Please keep changes focused and include clear steps to test where possible.

## License

See `LICENSE`.