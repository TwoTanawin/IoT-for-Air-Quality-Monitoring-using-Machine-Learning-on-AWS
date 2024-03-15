import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import RobustScaler
import numpy as np

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)  # Adjust output size

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size, device=x.device)  # Use x.device
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])
        return out

scaler = RobustScaler()

# Input data to be predicted
# input_data = np.array([[ 298.1, 308.6, 1551, 42.8, 0, 2]])  # Shape: (1, 6)

input_data = [[ 298.2,308.5,2678,10.7,86, 2]] # Shape: (1, 6) Failure

scaler.fit(input_data)

# Scale the input data using the same scaler used during training
input_data_scaled = scaler.transform(input_data)

# Convert the scaled data to a PyTorch tensor
input_tensor = torch.tensor(input_data_scaled, dtype=torch.float32)

# Reshape the input tensor to match the model's input shape (batch_size, seq_len, input_size)
input_tensor = input_tensor.unsqueeze(1)  # Assuming single data point, so seq_len = 1

# Load the saved model state dictionary
model_state = torch.load('/home/two-asus/Documents/cloudcomputing/project/ML/rnn_model.pth')

# Set hyperparameters based on the saved model
input_size = 6  # Example: adjust this to match your input size
hidden_size = 32  # Example: adjust this to match your hidden size
output_size = 2  # Example: adjust this based on your target classes

# Instantiate the model
model = RNN(input_size, hidden_size, output_size)

# Load the saved model state dictionary into the instantiated model
model.load_state_dict(model_state)

# Set the model to evaluation mode
model.eval()

# Perform inference
with torch.no_grad():
    output = model(input_tensor)

# Get the predicted class (assuming output is logits)
_, predicted_class = torch.max(output, 1)

# Convert tensor to NumPy array
predicted_label_array = predicted_class.numpy()

# Print the NumPy array
print(predicted_label_array)

# Access individual elements
for element in predicted_label_array:
    print(element)
