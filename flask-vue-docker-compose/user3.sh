#!/bin/bash

# Update package lists and install Docker
sudo apt-get update
sudo apt-get install docker.io -y

# Start Docker service
sudo systemctl start docker

# Run a Docker container (hello-world as an example)
sudo docker run hello-world

# Enable Docker to start on boot
sudo systemctl enable docker

# Add the current user to the docker group
sudo usermod -a -G docker $(whoami)
sudo usermod -aG docker $USER

# Pull Docker images from Docker Hub
# sudo docker pull twotanawin/air-quality-flaskapi:0.4
# sudo docker pull twotanawin/vue-air-quality-app:0.2

# Run another Docker container with specific settings
sudo apt-get update
sudo docker run --rm \
  --network=host \
  -p 5000:5000 \
  -p 80:80 \
  -e AWS_ACCESS_KEY_ID=YOURKYE \
  -e AWS_SECRET_ACCESS_KEY=YOURKYE \
  -e AWS_DEFAULT_REGION=YOURREGION \
  twotanawin/only-flask-app:0.1 \
  gunicorn -w 4 -b 0.0.0.0:80 app:app 

