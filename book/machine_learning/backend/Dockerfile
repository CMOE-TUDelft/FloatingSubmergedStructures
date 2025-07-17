# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir sentence-transformers
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('intfloat/e5-base')"


# Copy project files
COPY . .

# ✅ Copy vectorstore into the correct path
# (if it's already in project root, `COPY . .` does this — just verify path)
# If not, do something like:
COPY vectorstore_jupyterbook /vectorstore_jupyterbook

# Expose the port (Django default)
EXPOSE 8000

# Start the Django development server
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
