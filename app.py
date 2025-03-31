from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Load your model and vectorizer
    import joblib
    model = joblib.load("hate_speech_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

    # Transform text using the vectorizer
    text_vectorized = vectorizer.transform([text])

    # Predict class
    prediction = model.predict(text_vectorized)[0]

    # Class labels
    class_labels = {0: "Hate speech", 1: "Offensive", 2: "Non-toxic"}

    return jsonify({"prediction": class_labels[prediction]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Ensure this is running on 5000
