# Use the latest Amazon Linux image
FROM amazonlinux:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Accept build-time environment variable to differentiate between dev and prod
ARG ENVIRONMENT=prod

# Update the package list and install necessary packages
RUN dnf -y update && \
    dnf -y install python3 python3-pip git iputils && \
    dnf clean all

# Install pip packages
RUN pip3 install django boto3 django-storages psycopg2-binary gunicorn django-markdownx django-markdownify

# Create a non-root user
RUN adduser klaatubaradanikto

# Switch to the non-root user
USER klaatubaradanikto

# Set the working directory
WORKDIR /home/klaatubaradanikto

# Copy project into Docker container
COPY techronomicon /home/klaatubaradanikto

# Use a conditional statement to run different commands based on the environment
CMD if [ "$ENVIRONMENT" = "dev" ]; then \
        python3 manage.py runserver 0.0.0.0:8000; \
    else \
        gunicorn --bind 0.0.0.0:8000 --timeout 600 techronomicon.wsgi:application; \
    fi
