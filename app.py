from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('insurance.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        northwest = 0
        southeast = 0
        southwest = 0
        age = int(request.form['age'])
        bmi = int(request.form['bmi'])
        children = request.form['Children']
        Sex = request.form['Sex']
        Smoker = request.form['Smoker']
        region = request.form['Region']
        if(region == 0):
            northwest = 1
        elif(region == 1):
            southeast = 1
        elif(region == 2):
            southwest = 1
        prediction=model.predict([[age,bmi,children,Sex,Smoker,northwest,southeast,southwest]])
        return render_template('home.html',prediction_texts="Based on your personal details, you will be charged : "+str(round(prediction[0],2)))
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)

