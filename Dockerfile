# Use a python 3.11 base image
FROM python:3.11

# Install the required python packages
RUN pip install Flask==3.1.0 tensorflow==2.15 Pillow

# Create a directory inside the container for the project
WORKDIR /app

# Copy your model and inference server script into the container
COPY best_model.keras /app/best_model.keras
COPY inference_server.py /app/inference_server.py

# Expose the port the Flask app will run on
EXPOSE 5000

# Set the default command to run the inference server
CMD ["python", "inference_server.py"]
