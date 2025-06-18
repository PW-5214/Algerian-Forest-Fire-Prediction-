from flask import Flask,request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)

app = application
#import ridge regression model and standard scaler
ridge_model = pickle.load(open('model/ridge.pkl','rb'))
stand_scaler = pickle.load(open('model/scalar.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
         features = [float(request.form[key]) for key in ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'Classes']]
         new_data = stand_scaler.transform([features])
         result = ridge_model.predict(new_data)
         
         return render_template('home.html', results=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')