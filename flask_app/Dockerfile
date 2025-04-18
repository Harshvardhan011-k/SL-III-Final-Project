# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the dependencies in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Make the Flask app accessible on port 5000
EXPOSE 5000

# Set the environment variable to make the Flask app run in production mode
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
