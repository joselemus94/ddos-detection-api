# Real-Time Detection of Cloud-Based DDoS Attacks using AI

This project provides a Flask API to perform real-time detection of cloud-based DDoS attacks using trained AI models. It supports multiple classifiers including Random Forest, SVM, GBM, and KNN.

## 🔍 Overview

- **Dataset Used**: CIC-DDoS2019
- **Models**: Random Forest, Support Vector Machine, Gradient Boosting, K-Nearest Neighbors
- **Input**: Network traffic features (e.g., flow duration, packet size, IAT, etc.)
- **Output**: `0` for malicious traffic, `1` for benign

## 🚀 API Usage

### `/predict` (POST)
Make a prediction using one of the models.

#### Sample Request:

```json
{
  "features": [12345, 67.8, 0.003, 1, 200, 345, ...],
  "model": "random_forest"
}