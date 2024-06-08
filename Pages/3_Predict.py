import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title='Predict Page',
    layout='wide'
)

st.title('Make Customer Churn Predictions')


st.cache_resource()
def load_forest_pipeline():
    pipeline = joblib.load('./model/forest_pipeline.joblib')
    return pipeline


st.cache_resource()
def load_logistic_pipeline():
    pipeline = joblib.load('./model/logistic_pipeline.joblib')
    return pipeline


st.cache_resource(show_spinner='Models loading...')
def select_model():
    col1, col2 = st.columns(2)

    with col1:
        st.selectbox('select a model', options=['Random Forest', 'Logistic Regression'], key='selected_model')
    with col2:
        pass

    if st.session_state['selected_model'] == 'Random Forest':
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_logistic_pipeline()

    encoder = joblib.load('./model/encoder.joblib')

    return pipeline, encoder



