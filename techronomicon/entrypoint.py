#!/usr/bin/env python3
import subprocess
import sys


def run(*args):
    r = subprocess.run(args, check=False)
    if r.returncode != 0:
        sys.exit(r.returncode)


# Collect static using runtime env from .env/.env.docker
run("python", "manage.py", "collectstatic", "--noinput")

# Start gunicorn
run(
    "gunicorn",
    "techronomicon.wsgi:application",
    "--bind=0.0.0.0:8000",
    "--workers=3",
    "--threads=2",
)
