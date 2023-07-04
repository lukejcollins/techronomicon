# Use the latest Amazon Linux image
FROM amazonlinux:latest

# Maintainer information (optional)
LABEL maintainer="luke.collins@live.co.uk"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Update the package list and install necessary packages
RUN dnf -y update && \
    dnf -y install python3 python3-pip git && \
    dnf clean all

# Install pip packages
RUN pip3 install django boto3 django-storages

# Create a non-root user
RUN adduser klaatubaradanikto

# Switch to the non-root user
USER klaatubaradanikto

# Set the working directory
WORKDIR /home/klaatubaradanikto

# Make project directory
RUN mkdir techronomicon
