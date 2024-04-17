#!/bin/bash


set -e


ENVIRONMENT=JupyterSystemEnv
NOTEBOOK_FILE=/home/ec2-user/SageMaker/gb-training.ipynb


source /home/ec2-user/anaconda3/bin/activate "$ENVIRONMENT"


nohup jupyter nbconvert --ExecutePreprocessor.timeout=-1 --ExecutePreprocessor.kernel_name=python3 --to notebook --execute "$NOTEBOOK_FILE" &
jupyter nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute gb-training.ipynb


#source /home/ec2-user/anaconda3/bin/deactivate


