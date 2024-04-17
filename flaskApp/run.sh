sudo docker run --rm \
  --network=host \
  -p 5000:5000 \
  -p 80:80 \
  -e AWS_ACCESS_KEY_ID=YOURKYE \
  -e AWS_SECRET_ACCESS_KEY=YOURKYE \
  -e AWS_DEFAULT_REGION=YOURREGION \
  twotanawin/only-flask-app:0.1 \
  gunicorn -w 4 -b 0.0.0.0:80 app:app 