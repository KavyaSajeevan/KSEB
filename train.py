import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"\dataset\electricity_bill_dataset123.csv")  # Replace with your actual file path
labels = df.iloc[0]  # Assuming labels are in the first row
df = df[1:]  # Remove the first row (labels)
df.columns = labels  # Assign the labels to column names

# Convert dataframe to numpy array
data = df.values.astype(float)

# Splitting features and target variable
X = data[:, :-1]  # Features
y = data[:, -1]   # Target variable

# Normalize the features
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# Reshape the input to 3D array (samples, time steps, features)
X_reshaped = X_scaled.reshape(X_scaled.shape[0], 1, X_scaled.shape[1])

# Define the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_reshaped.shape[1], X_reshaped.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])  # Use 'mean_absolute_error' instead of 'mae'

# Define early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(X_reshaped, y, epochs=1, batch_size=32, validation_split=0.1, callbacks=[early_stopping])

# Save the trained model
model.save("electricity_bill_prediction_model.h5")
print("Model saved successfully.")

# Print training MAE after training
final_train_mae = history.history['mean_absolute_error'][-1]  # Use 'mean_absolute_error'
print(f"Final Training MAE: {final_train_mae}")

# Plot training & validation loss values
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(loc='upper left')
plt.show()

# Plot training & validation MAE values
plt.plot(history.history['mean_absolute_error'], label='Train MAE')  # Use 'mean_absolute_error'
plt.plot(history.history['val_mean_absolute_error'], label='Validation MAE')  # Use 'val_mean_absolute_error'
plt.title('Model Mean Absolute Error (MAE)')
plt.ylabel('MAE')
plt.xlabel('Epoch')
plt.legend(loc='upper left')
plt.show()
