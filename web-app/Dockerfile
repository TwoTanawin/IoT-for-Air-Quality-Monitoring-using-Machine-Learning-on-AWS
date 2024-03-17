# Use an official Node.js image as a base
FROM ubuntu:latest

# Set up timezone
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set the environment variables to avoid tzdata configuration prompt during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libgl1-mesa-glx \
    libglib2.0-0 \
    qtdeclarative5-dev \
    python3-pip \
    python3-dev \
    libxcb-xinerama0 \
    tk

RUN curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs 

RUN npm install -g @vue/cli
RUN npm create vite@latest

# Install additional Python libraries
RUN pip3 install -U torch 
RUN pip3 install -U scikit-learn \
    matplotlib \
    numpy \
    pandas \
    Pillow \
    opencv-python \
    Django \
    fastapi \
    Flask

# Set the working directory
WORKDIR /app

# Start a Bash shell by default when the container runs
CMD ["/bin/bash"]
