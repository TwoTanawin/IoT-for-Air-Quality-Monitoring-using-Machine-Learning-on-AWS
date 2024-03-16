import torch
import torch.nn as nn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import RobustScaler
import numpy as np

# Define FastAPI app
app = FastAPI()

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

class InputData(BaseModel):
    data: list

@app.post("/predict/")
async def predict(input_data: InputData):
    input_data = np.array(input_data.data)
    input_tensor = torch.tensor(input_data, dtype=torch.float32).unsqueeze(0)
    
    scaler = RobustScaler()
    scaler.fit(input_data)
    input_data_scaled = scaler.transform(input_data)
    
    input_tensor = torch.tensor(input_data_scaled, dtype=torch.float32).unsqueeze(0)
    
    model_state = torch.load('/home/two-asus/Documents/cloudcomputing/project/ML/rnn_model.pth')
    
    input_size = 6
    hidden_size = 32
    output_size = 2
    
    model = RNN(input_size, hidden_size, output_size)
    model.load_state_dict(model_state)
    model.eval()
    
    with torch.no_grad():
        output = model(input_tensor)
    
    _, predicted_class = torch.max(output, 1)
    predicted_label_array = predicted_class.numpy().tolist()  # Convert NumPy array to Python list
    
    return {"predicted_labels": predicted_label_array}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
