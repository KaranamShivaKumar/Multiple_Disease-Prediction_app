# -*- coding: utf-8 -*-
"""
Created on Wed May 14 20:58:35 2025

@author: karan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler


#loading the models
diadetes_model = pickle.load(open('PIMA_daibetics.sav','rb'))
heart_model = pickle.load(open('Heart_disease_model.sav','rb'))
parkison_model = pickle.load(open('parikson_disease.sav','rb'))
scaler = pickle.load(open('parikson_scaled.sav','rb'))
#Sidebar for Navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                          ['PIMA Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parikson Disease Prediction'],
                          icons=['activity','heart','person-standing'],
                          default_index=0)
    
#Diabetes Prediction Page
if (selected == 'PIMA Diabetes Prediction'):
    
    #Page title
    st.title("PIMA Diabetes Prediction Using Machine Learning")
    
    
    #getting the input data from User
    #columns for input fields
    col1,col2,col3 = st.columns(3) 
    
    with col1:
        Pregnancies=st.text_input('Enter Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Enter Glucode Level')
    with col3:
        BloodPressure = st.text_input('Enter Blood pressure level')
    with col1:
        SkinThickness = st.text_input("Enter the Skin thickness")
    with col2:
        Insulin = st.text_input("Enter the Insulin level")
    with col3:
        BMI = st.text_input("Enter the Body Mass Index")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Enter DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Enter the Age")
    
    #Code for the prediction
    diagnosis = ''
    
    #creating a Button for the Prediction
    if st.button('test result'):
        dia_prediction = diadetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFunction,Age]])
    
    
        if dia_prediction[0] == 1:
            diagnosis = "The Person is Diabetic"
        else:
            diagnosis ="The Person Not Diabetic"
    
    st.success(diagnosis)
    
if (selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title("Heart Disease Prediction Using Machine Learing")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

    
if (selected == 'Parikson Disease Prediction'):
    
    #Page title
    st.title("Parikson Disease Prediction Using Machine Learning")
    

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
    
        user_input = [float(x) for x in user_input]
    
        # Apply StandardScaler correctly
        scaled_input = scaler.transform([user_input])
    
        # Predict
        parkinsons_prediction = parkison_model.predict(scaled_input)
    
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"


    st.success(parkinsons_diagnosis)
