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
ENV SECRET_KEY=django-insecure-build-key-temporary

# Create staticfiles directory and collect static files with verbose output
RUN mkdir -p staticfiles && \
    python manage.py collectstatic --noinput --verbosity 2 && \
    ls -la staticfiles/ | head -20

# Expose port
EXPOSE 8080

# Run gunicorn
CMD ["gunicorn", "hospital.wsgi", "--bind", "0.0.0.0:8080", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-"]
