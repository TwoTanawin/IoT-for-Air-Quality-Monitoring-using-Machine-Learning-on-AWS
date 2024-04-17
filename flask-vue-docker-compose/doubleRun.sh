# Run Docker containers with specific settings
sudo docker run -d --rm \
  --network=host \
  -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=YOURKYE \
  -e AWS_SECRET_ACCESS_KEY=YOURKYE \
  -e AWS_DEFAULT_REGION=YOURREGION \
  twotanawin/air-quality-flaskapi:0.4 \
  gunicorn -w 4 -b 127.0.0.1:5000 app:app

sudo docker run --rm \
  --network=host \
  -p 3000:3000 \
  --name vue-air-quality-app \
  twotanawin/vue-air-quality-app:0.2