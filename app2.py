import streamlit as st
import pandas as pd
import pickle

# Load the model
load_model = pickle.load(open('model.pickle', 'rb'))

st.title("Covid classification using regression")

# Input fields
Cough_symptoms = st.radio("Cough Symptoms", ["True", "False"])
Fever = st.radio("Fever", ["True", "False"])
Sore_throat = st.radio("Sore throat", ["True", "False"])
Shortness_of_breath  = st.radio("Shortness of Breath", ["True", "False"])
Headache = st.radio("Headache", ["True", "False"])
Known_contact = st.radio("Known Contact", ['Abroad', 'Contact with confirmed', 'Other'])

# Convert string to boolean
Cough_symptoms = Cough_symptoms == "True"
Fever = Fever == "True"
Sore_throat = Sore_throat == "True"
Shortness_of_breath = Shortness_of_breath == "True"
Headache = Headache == "True"

# Encoding categorical variable
if Known_contact == 'Abroad':
    Known_contact = 0
elif Known_contact == 'Contact with confirmed':
    Known_contact = 1
else:
    Known_contact = 2

# Create DataFrame
df = pd.DataFrame({
    'Cough_symptoms': [Cough_symptoms],
    'Fever': [Fever],
    'Sore_throat': [Sore_throat],
    'Shortness_of_breath': [Shortness_of_breath],
    'Headache': [Headache],
    'Known_contact': [Known_contact]
})

# Submit button
if st.button("Submit"):
    prediction = load_model.predict(df)  # Assuming the model has a predict method
    st.write("Prediction:", prediction[0]) 