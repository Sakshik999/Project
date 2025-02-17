import streamlit as st
import pandas as pd
import pickle

load_model = pickle.load(open('model.pickle', 'rb'))

st.title("salary prediction using Regression")

age = st.number_input("enter age = ")
exp = st.number_input ("enter exp = ")
edu = st.radio ("education", ["Bachlor's","Master's", "PHD"])

if edu == "Bachlor's":
    b = 1;m = 0; p = 0
elif edu == "Master's":
    b = 0;m = 1; p = 0
else:
    b = 0;m = 0; p = 1

df = pd.DataFrame({
    'Age': [age],
    'Years of Experience':[exp],
    "Bachelor's": [b],
    "Master's":[m],
    "PhD":[p],
})
df
if st.button("Submit"):
    pred = load_model.predict(df)
    st.success("The data is submitted")
    st.write("The Salary is = ",pred)





