# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install necessary build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential libssl-dev libffi-dev python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5321

# Start the application using uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]
