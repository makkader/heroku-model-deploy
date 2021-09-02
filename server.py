from flask import Flask
import json
import pandas as pd

#from sklearn.datasets import make_moons
#import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.datasets import make_classification
import pickle

from flask import request, jsonify
import base64
import os


app = Flask(__name__)


users = {
    "datarobot": "apikey_for_datarobot",
    "other": "apikey_for_other"
}


def verify(username, password):
    if username in users and users.get(username) == password:
        return True
    return False


# Model preparation
model_file_name = "airline-sklearn.pkl"


def getModel():

    with open(model_file_name, 'rb') as pickled:
        model = pickle.load(pickled)
    return model


model = getModel()


def getPrediction(scoring_value):
    preds = model.predict(scoring_value).tolist()
    data = [{"predictionValues": [{"value": pred, "label": "score"}], "prediction": pred, "rowId": i} for i, pred in enumerate(preds)]

    return json.dumps({"data": data})

# end model preparation


@app.route('/')
def home():
    return 'I am listening!'


@app.route('/predict', methods=["GET", "POST"])
def predict():
    encoded_auth = request.headers['Authorization'].strip("Basic ")
    username, password = base64.b64decode(encoded_auth).decode("utf-8").split(":")
    if verify(username, password) == False:
        return "Unauthorized", 401

    data = request.json
    values = data['input_data'][0]['values']
    fields = data['input_data'][0]['fields']
    scoring_value = pd.DataFrame(values, columns=fields)
    response = getPrediction(scoring_value)
    return response, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
