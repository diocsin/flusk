from flask import Flask, request, jsonify
import pandas as pd

import spotify_service

app = Flask(__name__)

data = pd.read_csv("model/data.csv")


@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    prediction = spotify_service.recommend_songs(json_, data)
    return jsonify({'prediction': [1, 2, 3]})


if __name__ == '__main__':
    print("Тут")
    app.run(host='0.0.0.0', port=5000)
