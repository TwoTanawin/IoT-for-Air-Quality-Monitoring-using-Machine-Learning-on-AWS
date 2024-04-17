from flask import Flask, jsonify
import boto3
import joblib
import numpy as np
from flask_cors import CORS
from decimal import Decimal  # Import Decimal class for serialization

session = boto3.Session(region_name='ap-southeast-1')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def fetch_and_sort_items(table_name):
    try:
        dynamodb = boto3.resource('dynamodb',region_name='ap-southeast-1')
        table = dynamodb.Table(table_name)
        response = table.scan()

        items = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response['Items'])

        if items:
            sorted_items = sorted(items, key=lambda x: x['timestamp'], reverse=True)
            return sorted_items  # Return sorted items if there are any

    except Exception as e:
        print("An error occurred:", e)
        return []  # Return an empty list if there's an error or no items found

@app.route('/get_last_data', methods=['GET'])
def get_last_data():
    try:
        sorted_items = fetch_and_sort_items('pms3003_data')

        if sorted_items:
            latest_item = sorted_items[0]  # Latest item is now the first in the sorted list

            last_data = [int(value) for value in latest_item.values() if isinstance(value, Decimal)]
            return jsonify({'last_data': last_data})  # Return the data as JSON

        return jsonify({'error': 'No data found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_last_10_data', methods=['GET'])
def get_last_10_data():
    try:
        sorted_items = fetch_and_sort_items('pms3003_data')

        if sorted_items:
            last_10_items = sorted_items[:10]  # Get the last 10 items
            last_10_data = []
            count = 1  # Initialize count for numbering the entries

            for entry in last_10_items:
                entry.pop('station_number', None)
                data_values = [int(value) if isinstance(value, Decimal) else value for value in entry.values()]  # Convert Decimal to int if needed
                data_dict = {str(count): data_values}  # Create dictionary with numbered keys
                last_10_data.append(data_dict)
                count += 1

            return jsonify({'last_10_data': last_10_data})  # Return the modified data as JSON

        return jsonify({'error': 'No data found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_ML_prediction', methods=['GET'])
def get_ML_prediction():
    try:
        sorted_items = fetch_and_sort_items('pms3003_data')

        if sorted_items:
            latest_item = sorted_items[0]  # Latest item is now the first in the sorted list

            last_data = [int(value) for value in latest_item.values() if isinstance(value, Decimal)]

            # Create a boto3 client for accessing S3
            s3 = boto3.client('s3',region_name='ap-southeast-1')

            # Specify the S3 bucket name and the key of the model file
            bucket_name = 'tanawin-iot-mybucket'
            key = 'models/gb_classifier_model_nontune.pkl'

            try:
                # Download the model file from S3
                s3.download_file(bucket_name, key, 'gb_classifier_model_nontune.pkl')

                # Load the model from the downloaded file
                model = joblib.load('gb_classifier_model_nontune.pkl')

                class_names = ['Good', 'Moderate', 'Unhealthy for sensitive', 'Unhealthy', 'Hazardous']

                # Convert input data to numpy array and reshape
                new_data_reshaped = np.array(last_data).reshape(1, -1)

                # Make predictions on the new data
                predictions = model.predict(new_data_reshaped)

                # Map predicted class index to class name
                predicted_class_name = class_names[predictions[0]]

                return jsonify({'prediction': predicted_class_name})  # Return the predicted class name as JSON

            except Exception as e:
                return jsonify({'error': f'Error loading model: {str(e)}'}), 500

        return jsonify({'error': 'No data found'}), 404

    except Exception as e:
        return jsonify({'error': f'Error fetching and sorting items: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
