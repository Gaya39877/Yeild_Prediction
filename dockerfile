# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip before installing dependencies
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
