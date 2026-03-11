# Base Image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start Fast-API server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]