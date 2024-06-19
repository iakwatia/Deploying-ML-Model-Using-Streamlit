import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='History Page',
    layout='wide'
)

st.title('Prediction History')
st.write('This page displays the history of predictions made.')
csv_path= './data/history.csv'

if os.path.exists(csv_path):
    history_df = pd.read_csv('./data/history.csv')
    st.dataframe(history_df)

else:
    st.info('Make a prediction first')





# Set up the layout of the history page


# Display the prediction history as a table
