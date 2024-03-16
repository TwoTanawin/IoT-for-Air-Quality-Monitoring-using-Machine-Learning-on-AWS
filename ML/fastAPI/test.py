import requests

# Define the input data as a 2D array with one row and six columns
input_data = {
    "data": [[298.2, 308.5, 2678, 10.7, 86, 2]]
}

# Send a POST request to the FastAPI endpoint
response = requests.post("http://localhost:8000/predict/", json=input_data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the predicted labels returned by the API
    print("Predicted Labels:", response.json()["predicted_labels"])
else:
    print("Error:", response.text)
