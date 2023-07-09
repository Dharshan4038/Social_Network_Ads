import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open("log_reg.pkl","rb")
clf = pickle.load(pickle_in)


def predict_status(age,salary):
    pred = clf.predict([[age,salary]])
    return pred


st.title("Social Network Ads")
html_temp = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                   
                </head>
                <body>
                    <div class="container">
                        <h2>Social Network Ads with Streamlit</h2>
                    </div>
                </body>
                </html>
            """

st.markdown(html_temp,unsafe_allow_html=True)
age = st.number_input('Enter Age')
salary = st.number_input('Enter Salary')
result = ""

if st.button("Predict"):
    result = predict_status(age,salary)
st.success("The output is {}".format(result))

