Project 3 - Inference Server
============================

Overview
--------

This project involves building an inference server that classifies satellite images as "damaged" or "not damaged" based on a trained model. The server is built using **Flask** and **TensorFlow** and is packaged in a Docker container for ease of deployment.

Docker Image
------------

The inference server is packaged into a Docker image and hosted on **Docker Hub**. You can pull and run the image using the following command:

`docker pull onezavhora/onezavhora-project3-inference-server:current`

This Docker image contains the necessary environment, the pre-trained model, and the Flask server, allowing you to easily deploy the inference server on any machine with Docker installed.

### How to Run the Inference Server

Once you have the Docker image, you can start the inference server using **Docker Compose**. Make sure to clone this repository to your local machine, navigate to the project directory, and use the following steps to set up and run the server:

1.  **Build and run the Docker container:**

    `docker-compose up --build`

2.  **Stop the server:**

    To stop the server, use:

    `docker-compose down`

3.  **Access the server:**

    -   The server will run on port `5000` by default.

    -   You can access the summary of the model by making a `GET` request to `/summary`:

        `curl http://localhost:5000/summary`

    -   You can send an image to the `/inference` endpoint using a `POST` request:

        `curl -X POST -F "image=@path_to_image.jpg" http://localhost:5000/inference`

        Make sure to replace `path_to_image.jpg` with the path to the image you want to classify.

GitHub Repository
-----------------

The source code for this project, including the `Dockerfile`, `inference_server.py`, and other related files, is stored in this **GitHub repository**.

**GitHub Repository Link**: https://github.com/OnezaVhora/COE379L-Project-3

Docker Hub Repository
---------------------

The **Docker image** for the inference server is publicly available on **Docker Hub**. You can use it to quickly run the server without building it from source.

**Docker Hub Image**: `onezavhora/onezavhora-project3-inference-server:current`

Model Inference Details
-----------------------

The inference server provides the following two endpoints:

### 1\. `/summary` (GET)

-   **Description**: Returns metadata about the model (name, version, description, number of parameters, input/output shape).

-   **Example**:

    bash

    Copy code

    `curl http://localhost:5000/summary`

    Response:

    json

    Copy code

    `{
      "name": "Damaged Building Classifier",
      "version": "v1.0",
      "description": "A model to classify images of buildings as damaged or not damaged.",
      "number_of_parameters": 6351161,
      "input_shape": [null, 128, 128, 3],
      "output_shape": [null, 1]
    }`

### 2\. `/inference` (POST)

-   **Description**: Accepts an image file and returns the predicted label ("damage" or "no damage").

-   **Example**:

    `curl -X POST -F "image=@path_to_image.jpg" http://localhost:5000/inference`

    Response:

    `{
      "prediction": "damage"
    }`

Docker Hub Login (if necessary)
-------------------------------

If you want to push the image to your Docker Hub account, you will need to log in using your Docker credentials:

1.  **Login to Docker Hub**:

    `docker login`

2.  **Tag the Docker image** (if needed):

    `docker tag onezavhora/project3-inference-server:current onezavhora/onezavhora-project3-inference-server:current`

3.  **Push the image to Docker Hub**:

    `docker push onezavhora/onezavhora-project3-inference-server:current`

Conclusion
----------

This repository contains the necessary code and Docker configuration to deploy an inference server for classifying satellite images of damaged buildings. You can use the Docker image for quick deployment, and the provided API endpoints allow you to easily interact with the model.
