# docker run --rm -p 5000:5000 --name ml-app --network=host twotanawin/air-quality-flaskapi:0.1 

sudo docker run --rm \
  --network=host \
  -p 5000:5000 \
  -e AWS_ACCESS_KEY_ID=YOURKYE \
  -e AWS_SECRET_ACCESS_KEY=YOURKYE \
  -e AWS_DEFAULT_REGION=YOURREGION \
  twotanawin/air-quality-flaskapi:0.3 \
  gunicorn -w 4 -b 10.0.1.8:5000 app:app 