from flask import Flask, render_template, request, jsonify
from utils import make_prediction


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email = request.form.get("content")
    predictions = make_prediction(email)
    return render_template("index.html", predictions=predictions, email=email)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = make_prediction(email)
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction


if __name__ == "__main__":
    app.run(debug=True)