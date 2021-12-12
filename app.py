from flask import Flask, render_template, redirect, url_for,request
#from flask_bootstrap import Bootstrap
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField
#from wtforms.validators import DataRequired 
#import pandas as pd
#import numpy as np 
#from   sklearn.model_selection   import   train_test_split 
#import joblib
#from   sklearn.linear_model   import   LogisticRegression 
#from   sklearn.metrics   import   accuracy_score

app = Flask(__name__)
                                              
@app.route('/')                                
def hello_world():                                 
    return render_template('index.html')
@app.route('/predict/',methods = ["POST"])                    
def predict(): 
     if request.method == "POST" :
        input_data = [x  for x in request.form.items() ]
       # result = ml(input_data)
        
        return render_template("index.html", res=input_data)
     else :
         return "404 error"
         
def ml(input_data) :
    model = joblib.load("model.pkl")
    input_data_as_numpy_array= np.asarray(input_data)


    input_data_reshaped = input_data_as_numpy_array.reshape(  1  ,  -1  )

    prediction = model.predict(input_data_reshaped) 

    if  (prediction[ 0 ]==  0 ) : 
         result = 'The Person does not have a Heart Disease' 
    else : 
         result = 'The Person has Heart Disease' 
    return result
     
if __name__ == '__main__':
   app.run(debug=True)