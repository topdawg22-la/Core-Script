FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11

# Install system deps often needed by python-can backends
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# (Optional) Install SocketCAN utilities for Linux-based development
RUN apt-get update && apt-get install -y can-utils || true
