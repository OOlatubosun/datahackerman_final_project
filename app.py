## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

st.title('GOT Sentiment Prediction')

Friends = st.slider('Friends', 150, 350)
Status_count = st.slider('Status_count', 1500, 2500)
Verified = st.selectbox("Verified", options=["True", "False"])
Country = st.selectbox('Country', options=['GB', 'GG', 'JE'])
Platform = st.selectbox('Platform', options=["twitter"])
Text = st.selectbox('Text', options=["@smollyalexander thank u hunty"])
Latitude = st.slider('Latitude', 50.05, 60.05)
Longitude = st.slider('Longitude', -4.20, 4.20)

input_data_dict = {
    "Friends": 282,
    "Status_count": 2085,
    "Verified": "False",
    "Country": "GB",
    "Platform": "twitter",
    "Text": "@smollyalexander thank u hunty",
    "Latitude": 53.42,
    "Longitude": -2.92
}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = "models"

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("CLICK TO PREDICT GOT SENTIMENT")

if submit:

    got_sentiment = save_model_predictor.predict(input_data)[0]

    st.write(f"The predicted got sentiment is: {got_sentiment}")