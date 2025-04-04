import numpy as np
import pandas as pd
from keras.models import load_model
import pickle
from flask import session
import tensorflow as tf
import keras.backend as K

# Your specific data point
def predict_bill(input_data):
    # Clear any existing TensorFlow session/graph
    K.clear_session()
    
    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Load the model
    model = load_model('electricity_bill_model.h5')
    
    # Load the scaler
    with open('electricity_bill_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    # Scale the input data
    required_features = ['Fan', 'Refrigerator', 'AirConditioner', 'Television',
                        'Monitor', 'MotorPump', 'Temperature', 'Humidity',
                        'MonthlyHours', 'TariffRate']
    
    input_df = input_df[required_features]
    input_scaled = scaler.transform(input_df)
    
    # Make prediction - with TF 1.15, don't use verbose parameter
    prediction = model.predict(input_scaled).flatten()[0]
    
    # Print result
    print(f"Input data: {input_data}")
    print(f"Predicted Electricity Bill: ${prediction:.2f}")
    
    # Clear session data after prediction (if session is being used in your context)
    if 'session' in globals() and session:
        session.clear()  # This will clear the session data after processing
    
    return prediction
