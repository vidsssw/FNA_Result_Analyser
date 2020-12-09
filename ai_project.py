import streamlit as st
import streamlit_theme as stt
import base64
import joblib
import numpy as np
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

set_png_as_page_bg('bg2.png')
stt.set_theme({'primary': '#F794B9'})

st.markdown("<h1 style='text-align: center;'> FNA Result Analyser</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> An Accurate Tool for Breast Cancer Prediction </p>", unsafe_allow_html=True)

col1,col2,col3 = st.beta_columns(3)
with col1:
    area_se = st.number_input('Enter Area Standard Error')
with col2:
    area_mean = st.number_input('Enter Area Mean')
with col3:
    concavity_mean = st.number_input('Enter Concavity Mean')


col7,col8,col9 = st.beta_columns(3)
with col7:
    symmetry_worst = st.number_input('Enter Symmetry Worst')
with col8:
    smoothness_worst = st.number_input('Enter Smoothness Worst')
with col9:
    concavity_worst = st.number_input('Enter Concavity Worst')

def predict():
    loaded_model = joblib.load('finalized_cancer_model.sav')
    predictions=loaded_model.predict(np.array([area_mean,concavity_mean,area_se,smoothness_worst,concavity_worst,symmetry_worst]).reshape(1,-1))
    return predictions

col12, col13,col14 = st.beta_columns(3)




with col13:
    if st.button('Get Result'):
        with st.spinner('Predicting.....'):
            if predict() == 'B':
                st.markdown("<p style='text-align: center; color: green;'> Benign </p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='text-align: center; color: red;'> Malignant </p>", unsafe_allow_html=True)

        
   
            
            












    