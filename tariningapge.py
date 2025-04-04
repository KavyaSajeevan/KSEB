import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pickle

# Set random seed for reproducibility
np.random.seed(42)
tf.set_random_seed(42)  # Changed from tf.random.set_seed for TF 1.15

# Load the dataset
print("Loading and preprocessing data...")
data = pd.read_csv('electricity_bill_dataset123.csv')

# Display basic information about the dataset
print("\nDataset shape:", data.shape)
print("\nDataset preview:")
print(data.head())
print("\nDataset statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Split features and target
X = data.drop('ElectricityBill', axis=1)
y = data['ElectricityBill']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save the scaler for prediction
with open('electricity_bill_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Build the deep learning model
def build_model():
    model = Sequential()
    # Input layer with 64 neurons
    model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dropout(0.2))
    # Hidden layer with 32 neurons
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    # Hidden layer with 16 neurons
    model.add(Dense(16, activation='relu'))
    # Output layer (1 neuron for regression)
    model.add(Dense(1))
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Train the model
print("\nTraining the model...")
model = build_model()

# Define early stopping to prevent overfitting
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=20,
    restore_best_weights=True
)

history = model.fit(
    X_train_scaled, y_train,
    epochs=200,
    batch_size=16,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=1
)

# Save the trained model
model.save('electricity_bill_model.h5')
print("Model saved to 'electricity_bill_model.h5'")

# Evaluate the model
print("\nEvaluating the model...")
y_pred = model.predict(X_test_scaled).flatten()

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# Plot training history
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['mean_absolute_error'], label='Training MAE')  # Changed from 'mae' for Keras 2.2.4
plt.plot(history.history['val_mean_absolute_error'], label='Validation MAE')  # Changed from 'val_mae'
plt.title('Model MAE')
plt.ylabel('MAE')
plt.xlabel('Epoch')
plt.legend()

plt.tight_layout()
plt.savefig('training_history.png')
print("Training history plot saved to 'training_history.png'")

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('Actual Electricity Bill')
plt.ylabel('Predicted Electricity Bill')
plt.title('Actual vs Predicted Electricity Bill')
plt.savefig('prediction_results.png')
print("Prediction results plot saved to 'prediction_results.png'")

# Feature importance analysis
feature_importance = np.abs(model.layers[0].get_weights()[0]).mean(axis=1)
features = X.columns
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
importance_df = importance_df.sort_values('Importance', ascending=False)

print("\nFeature Importance:")
for index, row in importance_df.iterrows():
    print(f"{row['Feature']}: {row['Importance']:.4f}")

# Plot feature importance
plt.figure(figsize=(12, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'])
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Feature importance plot saved to 'feature_importance.png'")

print("\nTraining completed successfully!")