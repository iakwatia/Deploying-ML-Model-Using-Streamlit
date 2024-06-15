import streamlit as st
import pandas as pd
import joblib
import os
import datetime

#set up page config
st.set_page_config(
    page_title='Predict Page',
    layout='wide'
)

st.title('Make Customer Churn Predictions')


#load models
st.cache_resource()
def load_forest_pipeline():
    pipeline = joblib.load('./model/forest_pipeline.joblib')
    return pipeline


st.cache_resource()
def load_logistic_pipeline():
    pipeline = joblib.load('./model/logistic_pipeline.joblib')
    return pipeline


#define select model function
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

    #load encoder
    encoder = joblib.load('./model/encoder.joblib')

    return pipeline, encoder


if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None
if 'probability' not in st.session_state:
    st.session_state['probability'] =None

def make_prediction(pipeline, encoder):
    gender = st.session_state['gender']
    seniorcitizen = st.session_state['seniorcitizen']
    partner = st.session_state['partner']
    dependents = st.session_state['dependents']
    tenure = st.session_state['tenure']
    phoneservice = st.session_state['phoneservice']
    multiplelines = st.session_state['multiplelines']
    internetservice = st.session_state['internetservice']
    onlinesecurity = st.session_state['onlinesecurity']
    onlinebackup = st.session_state['onlinebackup']
    deviceprotection = st.session_state['deviceprotection']
    techsupport = st.session_state['techsupport']
    streamingtv = st.session_state['streamingtv']
    streamingmovies = st.session_state['streamingmovies']
    contract = st.session_state['contracttype']
    paperlessbilling = st.session_state['paperlessbilling']
    paymentmethod = st.session_state['paymentmethod']
    monthlycharges = st.session_state['monthlycharges']
    totalcharges = st.session_state['totalcharges']

    
    data = [[gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, internetservice, onlinesecurity, onlinebackup, 
             deviceprotection, techsupport, streamingtv, streamingmovies, contract, paperlessbilling, paymentmethod, monthlycharges, totalcharges]]
    

    columns = ['gender', 'seniorcitizen', 'partner', 'dependents', 'tenure', 'phoneservice', 'multiplelines', 'internetservice', 'onlinesecurity',
               'onlinebackup', 'deviceprotection', 'techsupport', 'streamingtv','streamingmovies','contract', 'paperlessbilling', 'paymentmethod',
               'monthlycharges', 'totalcharges']
    

    #create a dataframe
    df = pd.DataFrame(data, columns=columns)

   
    df['Prediction Time'] = datetime.date.today()
    df['Model Used'] = st.session_state['selected_model']
   

    df.to_csv('./data/history.csv', mode='a', header=not os.path.exists('./data/history.csv'), index=False)
    
    #make a prediction
    pred = pipeline.predict(df)
    pred_int = int(pred[0])
    prediction = encoder.inverse_transform([pred_int])

    
    # Get probabilities
    probability = pipeline.predict_proba(df)

    
    #update session state
    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability

    return prediction, probability 



def display_form():

    pipeline, encoder = select_model()

    with st.form('input-features'):

        col1, col2 = st.columns(2)

    with col1:
        st.write('#### Customer information')
        st.selectbox('Gender', options=['Male', 'Female'], key='gender')
        st.selectbox('Do you have a partner', options=['Yes', 'No'], key= 'partner')
        st.selectbox('Do you have any dependents', options=['Yes', 'No'], key='dependents')
        st.number_input('Enter your monthly charge', key='monthlycharges', min_value=10, max_value=200, step=1)
        st.number_input('Enter Tenure in months', key = 'tenure', min_value=0, max_value=72, step=1)
        st.number_input('Enter your totalcharge', key = 'totalcharges', min_value=10, max_value=1000, step=1)
        st.number_input('Enter one for senior citizen 0 for other', key = 'seniorcitizen', min_value=0, max_value=1)
        st.selectbox('What is your payment method', options=['Electronic Check','Mailed check', 'Bank transfer', 'Credit Card'],key='paymentmethod')
        st.selectbox('Select contract type', options=['Month-to-month', 'One year', 'Two year'], key= 'contracttype')
        
    with col2:
        st.write('#### Service information')
        st.selectbox('Do you have phone Service', options=['Yes', 'No'], key='phoneservice')
        st.selectbox('Do you have multiple lines', options=['Yes', 'No'], key='multiplelines')
        st.selectbox('Do you Have internet service', options=['DSL', 'fibre optic', 'No'], key='internetservice')
        st.selectbox('Do you have online security', options=['Yes', 'No'], key= 'onlinesecurity')
        st.selectbox('Do you have techsupport', options=['Yes', 'No'], key= 'techsupport')
        st.selectbox('Do you receive paperless billing', options=['Yes', 'No'], key= 'paperlessbilling')
        st.selectbox('Do you have device protection', options=['Yes', 'No'], key='deviceprotection')
        st.selectbox('Have you subscribed to streamingmovies', options=['Yes', 'No'], key='streamingmovies')
        st.selectbox('Have you subscribed to streamingtv', options=['Yes', 'No'], key='streamingtv')
        st.selectbox('Do you have online backup', options=['Yes', 'No'], key='onlinebackup')

        st.form_submit_button('Make Prediction', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))
   



if __name__ == '__main__':
    
    display_form()

    prediction = st.session_state['prediction']
    probability = st.session_state['probability']

    if not prediction:
        st.markdown("### Predictions will show here")
    elif prediction == "Yes":
        probability_of_yes = probability[0][1] * 100
        st.markdown(f"### You will lose the customer with a probability of {round(probability_of_yes, 2)}%")
    else:
        propability_of_no = probability[0][0] * 100
        st.markdown(f"### You will not lose the customer with a probability of {round(propability_of_no, 2)}%")

    st.write(st.session_state)