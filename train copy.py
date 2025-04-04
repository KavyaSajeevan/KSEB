import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv(r"D:\mybackup'\shemeem full back up\mes\kseb\kseb\dataset\electricity_bill_dataset123.csv")

# Replace "your_dataset.csv" with your dataset file path
labels = df.iloc[0]  # Assuming labels are in the first row
df = df[1:]  # Remove the first row (labels)
df.columns = labels  # Assign the labels to column names

# Convert dataframe to numpy array
data = df.values.astype(float)

# Splitting features and target variable
X = data[:, :-1]  # Features
y = data[:, -1]   # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the features
scaler = MinMaxScaler(feature_range=(0, 1))
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Reshape the input to 3D array (samples, time steps, features)
X_train_reshaped = X_train_scaled.reshape(X_train_scaled.shape[0], 1, X_train_scaled.shape[1])
X_test_reshaped = X_test_scaled.reshape(X_test_scaled.shape[0], 1, X_test_scaled.shape[1])

# Define the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Define early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(
    X_train_reshaped, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=1
)

# Evaluate the model on test data
test_loss, test_mae = model.evaluate(X_test_reshaped, y_test, verbose=0)

# Make predictions
y_pred_train = model.predict(X_train_reshaped).flatten()
y_pred_test = model.predict(X_test_reshaped).flatten()

# Calculate R-squared score (coefficient of determination)
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

# Calculate Mean Absolute Error
train_mae = mean_absolute_error(y_train, y_pred_train)
test_mae = mean_absolute_error(y_test, y_pred_test)

# Print accuracy metrics
print("\nModel Performance Metrics:")
print(f"Training R² Score: {train_r2:.4f}")
print(f"Testing R² Score: {test_r2:.4f}")
print(f"Training MAE: {train_mae:.4f}")
print(f"Testing MAE: {test_mae:.4f}")

# Calculate Mean Absolute Percentage Error (MAPE)
train_mape = np.mean(np.abs((y_train - y_pred_train) / y_train)) * 100
test_mape = np.mean(np.abs((y_test - y_pred_test) / y_test)) * 100
print(f"Training MAPE: {train_mape:.2f}%")
print(f"Testing MAPE: {test_mape:.2f}%")

# Save the trained model
model.save("electricity_bill_prediction_model.h5")
print("Model saved successfully.")

# Create a figure with 2 subplots
plt.figure(figsize=(12, 10))

# Plot 1: Training & validation loss
plt.subplot(2, 2, 1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss (MSE)')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')

# Plot 2: Training & validation MAE
plt.subplot(2, 2, 2)
plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.title('Model Mean Absolute Error')
plt.ylabel('MAE')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')

# Plot 3: Predicted vs Actual (Training)
plt.subplot(2, 2, 3)
plt.scatter(y_train, y_pred_train, alpha=0.5)
plt.plot([min(y_train), max(y_train)], [min(y_train), max(y_train)], 'r--')
plt.title('Predicted vs Actual (Training)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.text(0.05, 0.95, f'R² = {train_r2:.4f}', transform=plt.gca().transAxes)

# Plot 4: Predicted vs Actual (Testing)
plt.subplot(2, 2, 4)
plt.scatter(y_test, y_pred_test, alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
plt.title('Predicted vs Actual (Testing)')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.text(0.05, 0.95, f'R² = {test_r2:.4f}', transform=plt.gca().transAxes)

plt.tight_layout()
plt.show()