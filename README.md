# COE379L-Project-3

5. Instructions for Running and Stopping the Server
In your README or submission instructions, include these steps to start and stop the server using docker-compose:

Start the server:

To start the server, run the following command in the directory where your docker-compose.yml file is located:

bash docker-compose up --build
This command will build and start your Docker container. It will automatically map port 5000 inside the container to port 5000 on your local machine, making your API accessible at http://localhost:5000.

Stop the server:

To stop the server, use the following command:

bash docker-compose down
This will stop and remove the container.
