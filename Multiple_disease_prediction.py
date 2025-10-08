# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 14:36:55 2025

@author: admin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the models
st.markdown("""
    <style>
    /* Page background */
    .stApp {
        
         /* text color */
    }

    /* Input fields */
    .stTextInput input {
        background-color: #dce2ed;
        border: 1px solid ;
        border-radius: 8px;
        padding: 6px;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
    }
    </style>
""", unsafe_allow_html=True)


diabetes_model = pickle.load(open('C:/Users/admin/Desktop/Multiple Disease Predection/traindemodel/diabetes_model.sav', 'rb'))


heart_disease_model = pickle.load(open('C:/Users/admin/Desktop/Multiple Disease Predection/traindemodel/heart_disease_model.sav', 'rb'))

    
parkinson_model = pickle.load(open('C:/Users/admin/Desktop/Multiple Disease Predection/traindemodel/parkinsons_model.sav', 'rb'))

#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System ',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    #getting the data from the users
    #columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:    
        BloodPressure = st.text_input('Blood Pressure Value')
        
    with col1:  
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[
            int(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
            float(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)
        ]])
        
            if diab_prediction[0] == 1:
                diab_diagnosis = '⚠️ The Person is Diabetic'
            else:
                diab_diagnosis = '✅ The Person is not Diabetic'
    
        except ValueError:
            diab_diagnosis = '⚠️ Please enter valid numeric values!'
    
    st.success(diab_diagnosis)


#Diabetes Prediction Page
#if(selected == 'Heart Disease Prediction'):
    
    #page title
    #st.title('Heart Disease Prediction using ML')
    
# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # input fields in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain types (0-3)')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    
    with col1:
        thal = st.text_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)')
    
    # code for prediction
    heart_diagnosis = ''
    
    # button
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[
                int(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs),
                int(restecg), float(thalach), int(exang), float(oldpeak),
                int(slope), int(ca), int(thal)
            ]])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = '⚠️ The Person has Heart Disease'
            else:
                heart_diagnosis = '✅ The Person does not have Heart Disease'
        
        except ValueError:
            heart_diagnosis = '⚠️ Please enter valid numeric values!'
    
    st.success(heart_diagnosis)


    

# Parkinson's Prediction Page
if(selected == 'Parkinsons Prediction'):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    # input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        mdvp_apq = st.text_input('MDVP:APQ')
    with col4:
        dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')
    
    # code for prediction
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinson_model.predict([[
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                float(apq3), float(apq5), float(mdvp_apq), float(dda), float(nhr),
                float(hnr), float(rpde), float(dfa), float(spread1), float(spread2),
                float(d2), float(ppe)
            ]])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "⚠️ The Person has Parkinson's Disease"
            else:
                parkinsons_diagnosis = "✅ The Person does not have Parkinson's Disease"
        
        except ValueError:
            parkinsons_diagnosis = "⚠️ Please enter valid numeric values!"
    
    st.success(parkinsons_diagnosis)

    
    
    
    
    
    
    
    
    
    
    
    
    