import streamlit as st
import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(
    page_title='History Page',
    layout='wide'
)

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
 
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
 
name, authentication_status,username = authenticator.login(location='sidebar')
 
 
if st.session_state['authentication_status']:
    authenticator.logout(location='sidebar')

    if __name__ == '__main__':

        st.title('Prediction History')
    st.write('This page displays the history of predictions made.')
    csv_path= './data/history.csv'

    if os.path.exists(csv_path):
        history_df = pd.read_csv('./data/history.csv')
        st.dataframe(history_df)

    else:
        st.info('Make a prediction first')



elif st.session_state['authentication_status'] is False:
    st.error('Wrong username/password')
elif st.session_state['authentication_status'] is None:
    st.info('Login to get access to the app')
    st.code("""
    Test Account
    Username: iakwatia
    Password: 123456
    """)    
    st.write(st.session_state)



