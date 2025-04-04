import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

# Load the trained LSTM model
model = load_model("electricity_bill_prediction_model.h5")  # Load the saved model file

# Define default input values for prediction
import numpy as np

# Define default input values for prediction
default_input = np.array([[8,17,2,4,1,0,17.99,74.7,427,8.3]])  # Add an additional feature with value 0 to match the expected shape

# Reshape the input data if needed
default_input_reshaped = default_input.reshape(default_input.shape[0], 1, default_input.shape[1])

# Make predictions using the trained LSTM model
predicted_bill = model.predict(default_input_reshaped)

# Display the predicted electricity bill
print("Predicted electricity bill:", predicted_bill[0][0])
