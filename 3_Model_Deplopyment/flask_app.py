import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', colours)

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    #Convert the 0 and 1 back to Yes / No
    yn = {'1': 'Yes','0': 'No'}
    
    home_yn = yn[str(int_features[0])]
    manhattan_yn = yn[str(int_features[1])]
    accomidation = int_features[2]
    bedrooms = int_features[3]
    bathrooms = int_features[4]
    guests_included = int_features[5]
    
    return render_template('index.html', 
                           prediction_text=output,
                           home_yn=home_yn,
                           manhattan_yn=manhattan_yn,
                           accomidation=accomidation,
                           bedrooms=bedrooms,
                           bathrooms=bathrooms,
                           guests_included=guests_included)


if __name__ == "__main__":
    app.run(debug=True)