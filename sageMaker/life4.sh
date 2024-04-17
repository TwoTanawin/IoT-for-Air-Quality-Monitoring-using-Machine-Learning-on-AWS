set -e
ENVIRONMENT=python3
NOTEBOOK_FILE="/home/ec2-user/SageMaker/schedule_script.ipynb"
AUTO_STOP_FILE="/home/ec2-user/SageMaker/auto-stop.py"

echo "Activating conda env"
source /home/ec2-user/anaconda3/bin/activate "$ENVIRONMENT"
echo "Starting notebook"
nohup jupyter nbconvert  --to notebook --inplace --ExecutePreprocessor.timeout=600 --ExecutePreprocessor.kernel_name=python3 --execute "$NOTEBOOK_FILE" &
echo "Deactivating conda env"
source /home/ec2-user/anaconda3/bin/deactivate

# PARAMETERS
IDLE_TIME=600 # 10 minutes

echo "Starting the SageMaker autostop script in cron"
(crontab -l 2>/dev/null; echo "*/1 * * * * /usr/bin/python $AUTO_STOP_FILE --time $IDLE_TIME --ignore-connections") | crontab -

# Stop the instance after 10 minutes
sleep $IDLE_TIME
sudo shutdown -h now
