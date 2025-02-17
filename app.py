import streamlit as st
import sklearn as sk
import pickle
import pandas as pd
# import pickle
load_model = pickle.load(open('model.pickle', 'rb'))

st.title('Text Classification')
news = st.text_area("Enter News")
input_news = pd.DataFrame({
    'news':[news]
})
if st.button("Submit"):
    pred = load_model.predict(input_news['news'])

    st.success("The news is submitted")
    st.write("The news category = ",pred)
    st.balloons()
    
