from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
#load image - get image from request
#image -> tensor - transform to a tensor
#Make a prediction
#return json
    return jsonify({'result': 1})
