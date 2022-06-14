import pickle
import pandas as pd
import numpy as np
from churn.Churn import Churn
from flask import Flask, request, Response

# loading model
model = pickle.load(open('/Users/brunoschirmer/Repos/churn/src/model.pkl', 'rb'))

# initialize API
app = Flask(__name__)

@app.route('/churn/predict', methods=['POST'])
def churn_predict():
    test_json = request.get_json()
   
    if test_json: # there is data
        if isinstance(test_json, dict): # unique example
            data = pd.DataFrame(test_json, index=[0])
            original_data = data.copy()
            
        else: # multiple example
            data = pd.DataFrame(test_json, columns=test_json[0].keys())
            original_data = data.copy()
            
        # Instantiate class
        pipeline = Churn()
        
        # data preparation
        data = pipeline.data_preparation(data)
        
        # prediction
        data_prediction = pipeline.get_prediction(model, original_data, data)
        
        return data_prediction
        
        
    else:
        return Reponse('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0')