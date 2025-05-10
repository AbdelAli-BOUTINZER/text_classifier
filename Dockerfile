# Use a lightweight Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /api

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install spaCy English model
RUN python -m spacy download en_core_web_sm

# Copy the whole project into the container
COPY . .

# Expose the API port
EXPOSE 8000

# Command to run the API server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
