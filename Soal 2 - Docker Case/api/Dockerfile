# Use `python:3.11.4` as the base image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the FastAPI application code into the container
COPY ./api.py /app/api.py

# Start the FastAPI app using Uvicorn on host 0.0.0.0 and port 6000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "6000"]