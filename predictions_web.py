# -*- coding: utf-8 -*-

import numpy as np
import pickle
from flask import Flask, request, render_template
import random

# Load ML model
model = pickle.load(open('/Users/priyarao/Desktop/Test/lr_clf.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('AML_PROJ.HTML')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [str(i) for i in request.form.values()]
    print(features)
    my_list = [1]*74
    employee_name = ['COGNIZANT TECHNOLOGY SOLUTIONS US CORP','TATA CONSULTANCY SERVICES LIMITED','CAPGEMINI AMERICA INC','Google LLC','Ernst & Young U.S. LLP','INFOSYS LIMITED','DELOITTE CONSULTING LLP','AMAZON.COM SERVICES LLC']
    soc_title = ['Software Developers, Applications','Computer Systems Analysts','Computer Occupations, All Other','Software Developers, Systems Software','Computer Programmers','Operations Research Analysts','Computer Systems Engineers/Architects','Database Administrators']
    job_title =['SOFTWARE ENGINEER','SOFTWARE DEVELOPER','DATA ANALYST','DATA ENGINEER','SENIOR SOFTWARE ENGINEER','BUSINESS ANALYST','SYSTEMS ANALYST']
    work_state = ['CALIFORNIA','TEXAS','NEW YORK','MASSACHUSETTS','GEORGIA','NORTH CAROLINA']
    wage_category = ['MEDIUM','HIGH','VERY HIGH']
    
    if request.form['Employer_Name'] in employee_name and request.form['SOC_Title'] in soc_title and request.form['Job_Title'] in job_title and request.form['Work_state'] in  work_state and request.form['WAGE_CATEGORY'] in wage_category:
        op = 1
    else:
        op = 0   

    print(op)
    
    # Convert features to array
    array_features = [np.array(my_list)]
    print("features",array_features)
    # Predict features
    prediction = model.predict(array_features)
    print(prediction)
    output = prediction
    #if len(features) >0:
    #    output = 1
    #print(output)
    # Check the output values and retrive the result with html tag based on the value
    if op == 1:
        return render_template('AML_PROJ.HTML', 
                               result = 'You are likely to get your H1-B approved!')
    else:
        return render_template('AML_PROJ.HTML', 
                               result = 'Unfortunately,you are unlikely to get your H1-B approved!')

if __name__ == '__main__':
#Run the application
    app.run()
    
    