import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(variance, skewness, curtosis, entropy):

    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Enter Here")
    skewness = st.text_input("skewness","Enter Here")
    curtosis = st.text_input("curtosis","Enter Here")
    entropy = st.text_input("entropy","Enter Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()