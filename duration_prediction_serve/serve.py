import pickle
import os
from flask import Flask, request, jsonify

default_model_file = '../models/model-2022-01.bin'
MODEL_PATH = os.getenv('MODEL_PATH', default_model_file)

with open(MODEL_PATH, 'rb') as f_in:
    model = pickle.load(f_in)

# "feature engineering"
def prepare_features(ride): # just turns categorical features from ineger into string
    features = {}
    features['PULocationID'] = str(ride['PULocationID'])
    features['DOLocationID'] = str(ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

app = Flask('duration-prediction')

def predict(features):
    prediction = model.predict(features)
    return prediction[0]

# def post_process(pred):
#     return

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    trip = request.get_json() # because get in json object

    features = prepare_features(trip)
    pred = predict(features)
    # if we had post-processing it'd go here
    # result = post_process(pred)

    VERSION = os.getenv('VERSION', 'N/A')

    result = {
        'prediction': {
            'duration': pred,
        },
        'version': VERSION
    }

    return jsonify(result) # return json object

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)