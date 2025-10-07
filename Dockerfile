# Base image for Python and Ollama
FROM python:3.11-slim-bullseye AS base

# Install dependencies for Ollama
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama server
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy FastAPI application files
COPY ./pip-requirements.txt /app/requirements.txt
COPY . /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r /app/apps/api/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
RUN pip3 install -e .

# Expose ports for FastAPI and Ollama
EXPOSE 8000 11434

# Start Ollama server and ensure it is running before pulling models    
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull smollm2:1.7b && uvicorn app:app --host 0.0.0.0 --port 8000 --reload"]
