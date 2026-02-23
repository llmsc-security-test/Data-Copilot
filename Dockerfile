# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for matplotlib fonts
RUN apt-get update && apt-get install -y --no-install-recommends \
    fontconfig \
    fonts-dejavu \
    fonts-wqy-microhei \
    fonts-wqy-zenhei \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -g 1000 appuser && useradd -u 1000 -g appuser -m appuser

# Upgrade pip and install setuptools first
RUN pip install --no-cache-dir --upgrade pip setuptools

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY *.py ./

# Copy entrypoint script
COPY entry_point.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose the default Gradio port
EXPOSE 7860

# Set environment variables
ENV GRADIO_SERVER_NAME="0.0.0.0"
ENV GRADIO_SERVER_PORT=7860

# Run the Gradio app via entrypoint
ENTRYPOINT ["/entrypoint.sh"]
