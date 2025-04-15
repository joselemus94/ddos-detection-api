# app.py

from flask import Flask, request, jsonify
import joblib
import numpy as np
import time

app = Flask(__name__)

# Load all 4 models
models = {
    "random_forest": joblib.load("random_forest.pkl"),
    "svm": joblib.load("svm.pkl"),
    "gbm": joblib.load("gbm.pkl"),
    "knn": joblib.load("knn.pkl")
}

# Load scaler if used during training
# scaler = joblib.load("scaler.pkl")  # Uncomment if needed

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is up and running!"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Required fields
    try:
        features = np.array(data['features']).reshape(1, -1)
        model_choice = data.get('model', 'random_forest')
        model = models.get(model_choice)

        if model is None:
            return jsonify({"error": "Model not found"}), 400

        # Apply scaling if used during training
        # features = scaler.transform(features)

        start_time = time.time()
        prediction = model.predict(features)
        elapsed_time = time.time() - start_time

        return jsonify({
            "model": model_choice,
            "prediction": int(prediction[0]),
            "elapsed_time": f"{elapsed_time:.4f} seconds"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)