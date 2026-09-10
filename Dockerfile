FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Set environment variables for production
ENV DEBUG=False
ENV PYTHONUNBUFFERED=1

# Collect static files - with error handling
RUN mkdir -p staticfiles && \
    echo "Starting collectstatic..." && \
    python manage.py collectstatic --noinput --verbosity 3 2>&1 || true && \
    echo "collectstatic completed" && \
    echo "Listing staticfiles directory:" && \
    ls -lah staticfiles/ || echo "staticfiles directory empty or not found"

# Expose port
EXPOSE 8080

# Run gunicorn with proper logging
CMD ["gunicorn", "hospital.wsgi", "--bind", "0.0.0.0:8080", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"]
