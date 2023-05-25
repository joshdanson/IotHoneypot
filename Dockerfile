# This file is used to build the docker image for the iot_pot application locally

# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /iot_pot

# Create the logs directory
RUN mkdir logs



# Install any needed packages specified in requirements.txt
RUN pip install aiocoap

# Copy the rest of the application files into the container
COPY . .

# Make the script executable
RUN chmod +x iot_server.py
RUN chmod +x iot_client.py

# Expose the server and client ports used in your script
EXPOSE 5683 5684

# Run the script when the container is started
CMD ["python", "iot_server.py", "iot_client.py"]
