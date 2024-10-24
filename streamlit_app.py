import streamlit as st
import numpy as np
import string
import pickle
import requests

from io import BytesIO

model_url = 'https://drive.google.com/uc?id=1Ro3-Z9wQrRFmR_LTd72jLTizPNhsRDnY'
response = requests.get(model_url)
model_file = BytesIO(response.content)

# Load the model
model = pickle.load(open('crop_yield_model.pkl','rb'))

# URL of your model file hosted on GitHub
#url = "https://drive.google.com/uc?id=1Ro3-Z9wQrRFmR_LTd72jLTizPNhsRDnY"
# Download the model file
#response = requests.get(url)
#open('crop_recommendation.py', 'wb').write(response.content)

# Load the model
#with open('crop_recommendation.py', 'rb') as model_file:
#    model = pickle.load(open('crop_yield_model.pkl','rb'))



st.title("🌱Farming Crop Recommendation")
st.write("This is an app which will tell you which crop to plant based on the given answers to certain parameters.")
st.write("A random forest classifier was used.")

Soil_Type = st.radio("What is the soil type?:",["Peaty", "Loamy", "Sandy", "Saline", "Clay"])
Soil_pH = st.slider("Input the Soil's pH level:",5.5,8.0)
Temperature = st.slider("Input the average temperature: ",-3.0,55.0)
Humidity = st.slider("Input the average humidity level: ",45.0,80.0)
Wind_Speed = st.slider("Input the average wind speed: ",-4.0,22.0)

inputs = [[Soil_Type,Soil_pH,Temperature,Humidity,Wind_Speed]]

if st.button("Recommend!"):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(int)

    if updated_res == 0:
        st.write("Wheat")
    elif updated_res == 1:
        st.write("Corn")
    elif updated_res == 2:
        st.write("Rice")
    elif updated_res == 3:
        st.write("Barley")
    elif updated_res == 4:
        st.write("Sunflower")
    elif updated_res == 5:
        st.write("Soybean")
    elif updated_res == 6:
        st.write("Cotton")
    elif updated_res == 7:
        st.write("Sugarcane")
    elif updated_res == 8:
        st.write("Tomato")
    elif updated_res == 9:
        st.write("Potato")
    else: 
        st.write("Not applicable")
