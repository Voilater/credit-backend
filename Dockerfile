# Use a minimal base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

EXPOSE 8080

# Default command
CMD ["python", "app.py"]
