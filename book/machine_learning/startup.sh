#!/bin/bash

# Step 1: Start all services in the background
echo "Starting Docker Compose services..."
docker compose up -d

# Step 2: Wait for the Ollama container to become healthy
echo "Waiting for Ollama to start..."

# Optional: loop until the container is running (adjust timeout if needed)
until docker exec ollama ollama list &>/dev/null; do
  echo "Waiting for ollama container to respond..."
  sleep 2
done

# Step 3: Run the model
echo "Running phi3 model inside the ollama container..."
docker exec -it ollama ollama run phi3