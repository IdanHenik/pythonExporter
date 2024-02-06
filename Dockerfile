# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV API_URL=https://example.com/api/v2/
ENV API_TOKEN=your_default_token

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY source-code/* /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable

# Run app.py when the container launches
CMD ["python", "HUBexporter.py"]