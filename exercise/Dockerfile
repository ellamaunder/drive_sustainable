# Base image from node preinstalled 
FROM python:3.10-slim

# Set wroking directory where commands will be run
WORKDIR /app

# Copy over files 
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the app
EXPOSE 5000 

# Run the application when the container starts
CMD ["python", "api.py"]

