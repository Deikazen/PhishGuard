from flask import request, jsonify
from app.services.ml_service import predict_url

def predict():
    data = request.get_json()
    url = data.get("url")
    result = predict_url(url)
    return jsonify(result)

