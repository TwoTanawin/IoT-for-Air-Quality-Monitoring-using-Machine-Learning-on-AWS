import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
import numpy as np


# class RNN(nn.Module):
#     def __init__(self, input_size, hidden_size, output_size):
#         super(RNN, self).__init__()
#         self.hidden_size = hidden_size
#         self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
#         # Adjust the size of the fully connected layer to match the saved model
#         self.fc = nn.Linear(hidden_size, 2)  # Change output size to 2

#     def forward(self, x):
#         h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
#         out, _ = self.rnn(x, h0)
#         out = self.fc(out[:, -1, :])
#         return out

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)  # Adjust output size

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        out = self.fc(out[:, -1, :])
        return out



# Load and preprocess the input data
df = pd.read_csv('/home/two-asus/Documents/cloudcomputing/project/ML/data/predictive_maintenance.csv')
df.dropna(inplace=True)
df = df[~df.isin([np.nan, np.inf, -np.inf]).any(axis=1)]

labelEncode = LabelEncoder()
X = df.drop(['UDI','Product ID', 'Type', 'Target', 'Failure Type'], axis=1)  # Features
y = df['Target'] 
# X['Product ID'] = labelEncode.fit_transform(df['Product ID'])
X['Type'] = labelEncode.fit_transform(df['Type'])
encoded_data = X[['Type']]
X = pd.concat([X], axis=1)

# Split the data into training and testing sets (you may not need this for inference)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using RobustScaler (you may not need this for inference)
scaler = RobustScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert data to PyTorch tensors for inference
input_data = torch.tensor(X_test_scaled, dtype=torch.float32)  # Example: use X_test_scaled for inference

# Reshape the input tensor for inference (batch_size, seq_len, input_size)
input_data = input_data.unsqueeze(1)  # Assuming single data point, so seq_len = 1

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
    output = model(input_data)

# Get the predicted class (assuming output is logits)
_, predicted_class = torch.max(output, 1)

# Decode the predicted class using LabelEncoder
# predicted_label = labelEncode.inverse_transform(predicted_class.numpy())
# # Convert tensor to NumPy array
predicted_label_array = predicted_class.numpy()

# Print the NumPy array
print(predicted_label_array)

# Access individual elements
i = 0

for element in predicted_label_array:
    i +=  1
    print(i,element)