#!/bin/bash
set -e

# Set environment variables for Gradio
export GRADIO_SERVER_NAME="0.0.0.0"
export GRADIO_SERVER_PORT="${GRADIO_PORT:-7860}"

echo "Starting Data-Copilot on port ${GRADIO_PORT:-7860}..."

# Run the application
exec python app.py
