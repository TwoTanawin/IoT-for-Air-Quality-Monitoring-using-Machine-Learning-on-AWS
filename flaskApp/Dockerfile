# Use Python 3.10 base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Install AWS CLI
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    aws --version  # Verify AWS CLI installation

RUN curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt install nodejs
RUN node -v
RUN npm ci

# Expose the port that your Flask app runs on
EXPOSE 5000

# Command to run the Gunicorn server with AWS CLI configuration
CMD ["sh", "-c", "aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID && \
                  aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY && \
                  aws configure set region $AWS_DEFAULT_REGION && \
                  gunicorn -w 4 -b 0.0.0.0:5000 app:app"]