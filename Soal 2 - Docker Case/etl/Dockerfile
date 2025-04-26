# Use `python:3.11.4` as the base image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the etl application code into the container
COPY ./etl.py /app/etl.py

# Define the command to run the script
CMD ["python", "etl.py"]