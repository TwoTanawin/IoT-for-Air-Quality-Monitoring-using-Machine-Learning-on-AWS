# /home/two-asus/Documents/AI-Center/Dokcer/ultralytics


# Run the Docker container and start an interactive terminal session with volume sharing
docker run -it --rm \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /D/AIT/ICT/cloud-computing/IoT-for-Air-Quality-Monitoring-using-Machine-Learning-on-AWS/web-app:/app \
    -e XAUTHORITY=$XAUTHORITY \
    -v $XAUTHORITY:$XAUTHORITY \
    --network=host \
    my_web_cc

