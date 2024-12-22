# Credit Card Fraud Detection

This project focuses on detecting fraudulent transactions using a dataset of European cardholders' transactions during September 2013. Various machine learning algorithms were employed to build predictive models, and the performance was evaluated on both upsampled and downsampled datasets. The highest accuracy was achieved using the XGBoost model.

## Features

**Dataset:** Contains transaction data of European cardholders from September 2013.

**Machine Learning Models:**

Convolutional Neural Network (CNN)

Decision Tree

Gradient Boosting

K-Nearest Neighbors (KNN)

LightGBM

Logistic Regression

Long Short-Term Memory (LSTM)

Naive Bayes

Support Vector Machine (SVM)

Voting Classifier

XGBoost

**Performance Metrics:** Accuracy scores are calculated for both upsampled and downsampled datasets.

**Results:** Results are stored in results.txt, detailing the performance of each model.

## Highlights

**Best Model:** XGBoost achieved the highest accuracy:

Downsampled Dataset: **94.71%**

Upsampled Dataset: **99.99%**

_Project Structure_

server.py: Flask-based backend for serving predictions.

XGBoost/xgboost_upsampling_model.joblib: Pretrained XGBoost model file.

results.txt: Contains detailed evaluation results for all models.

requirements.txt: Lists all necessary dependencies.

## Usage

### Model Prediction:

The server.py script serves a /predict endpoint.

Send a JSON payload with transaction data to receive predictions.

Example payload:

{
"data": [1.0, 0.5, -0.1, ...] // Add values for all required features
}

### Run the Flask Server:

python server.py

## Analyze Results:

View detailed model performance in results.txt.

## Results

**Model Performance:** Detailed accuracy scores for each model on upsampled and downsampled datasets are available in results.txt.

**XGBoost:** Achieved the best accuracy for fraud detection.

## Future Enhancements

Implement real-time fraud detection with live data streams.

Experiment with ensemble techniques to combine multiple models for improved accuracy.

Integrate additional features such as geographic and temporal data to enhance predictive power.
