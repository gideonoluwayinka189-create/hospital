#!/bin/bash
set -e

echo "==== Starting Django collectstatic ===="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Django version: $(python -m django --version)"
echo ""

echo "Checking if STATIC_ROOT exists..."
mkdir -p staticfiles
echo "STATIC_ROOT ready at: $(pwd)/staticfiles"
echo ""

echo "Running: python manage.py collectstatic --noinput --verbosity 3"
python manage.py collectstatic --noinput --verbosity 3

echo ""
echo "==== Collectstatic completed ===="
echo "Checking collected files:"
ls -la staticfiles/ | head -30

echo ""
echo "Static files collected successfully!"
