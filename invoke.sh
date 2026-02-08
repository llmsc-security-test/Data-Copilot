#!/bin/bash

# Data-Copilot Docker invocation script
# Port mapping: 11440 (host) -> 7860 (container)

# Configuration
CONTAINER_NAME="data-copilot"
HOST_PORT=11440
CONTAINER_PORT=7860
IMAGE_NAME="data-copilot:latest"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker first."
    exit 1
fi

# Check if container is already running
if docker ps | grep -q "$CONTAINER_NAME"; then
    echo "Container '$CONTAINER_NAME' is already running."
    echo "To restart it, run: docker restart $CONTAINER_NAME"
    exit 0
fi

# Run the container
docker run -d \
    --name "$CONTAINER_NAME" \
    -p "$HOST_PORT:$CONTAINER_PORT" \
    -e GRADIO_SERVER_NAME="0.0.0.0" \
    -e GRADIO_SERVER_PORT="$CONTAINER_PORT" \
    --restart unless-stopped \
    "$IMAGE_NAME"

echo "Data-Copilot started successfully!"
echo "Access the application at: http://localhost:$HOST_PORT"
echo "To stop the container: docker stop $CONTAINER_NAME"
echo "To view logs: docker logs -f $CONTAINER_NAME"
