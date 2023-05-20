# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install system packages needed by ffmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*


# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt gunicorn


# Copy the rest of the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5321

# Start the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5321", "--timeout", "1200", "app:app"]

