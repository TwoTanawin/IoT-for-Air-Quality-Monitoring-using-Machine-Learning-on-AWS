import requests

# Define the base URL for the API
base_url = 'http://192.168.1.103:5000/'

# Test the '/get_last_data' endpoint
response = requests.get(base_url + 'get_last_data')
print('GET /get_last_data Response:')
print(response.json())
print()

# Test the '/get_last_10_data' endpoint
response = requests.get(base_url + 'get_last_10_data')
print('GET /get_last_10_data Response:')
print(response.json())
print()

# Test the '/get_ML_prediction' endpoint
response = requests.get(base_url + 'get_ML_prediction')
print('GET /get_ML_prediction Response:')
print(response.json())
print()
