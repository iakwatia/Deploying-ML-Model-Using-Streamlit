import streamlit as st
import pyodbc 
import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth



st.set_page_config(
    page_title='Data Page',
    layout='wide'
)

st.title('Telco Customer Churn Database')

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
 
 
    def filter_columns(data):
        # Allow the user to select the data type to display
        data_type = st.selectbox('Select Data type', [
                                'All', 'Numeric Columns', 'Categorical Columns'])
 
        if data_type == 'Numeric Columns':
            data = data.select_dtypes(include=['number'])
        elif data_type == 'Categorical Columns':
            data = data.select_dtypes(include=['object', 'category'])
 
        # Display the filtered data in Streamlit
        st.write('Filtered Data:', data)
 
 
    # Define the path to the dataset
    dataset_path = './data/train1.csv'
 
    # Check if the file exists
    if not os.path.isfile(dataset_path):
        st.error(
            f"The file '{dataset_path}' does not exist. Please check the path.")
    else:
        try:
            # Load the dataset
            data = pd.read_csv(dataset_path)
            # st.write('Loaded Data:', data)
            # Call the function to filter and display columns
            filter_columns(data)
        except Exception as e:
            st.error(f"Error loading the file '{dataset_path}': {e}")
 
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
 
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            # st.write('Loaded Data:', data)
            # Call the function to filter and display columns
            filter_columns(data)
        except Exception as e:
            st.error(f"Error loading the uploaded file: {e}")
 
 
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

# @st.cache_resource(show_spinner='connecting to database...')
# def init_connection():
#     return pyodbc.connect(
#         "DRIVER={SQL Server};SERVER="
#         + st.secrets['SERVER']
#         + ";DATABASE="
#         + st.secrets['DATABASE']
#         + ";UID="
#         + st.secrets['USERNAME']
#         + ";PWD="
#         + st.secrets['PASSWORD']

#     )

# connection = init_connection()

# @st.cache_data(show_spinner='running_query...')
# def running_query(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         #st.write(cursor.description)
#         df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])

#     return df


# def get_all_column():
#     sql_query = " SELECT * FROM LP2_Telco_churn_first_3000"
#     return running_query(sql_query)

# df = get_all_column() 



# numerical_columns = df.select_dtypes(include=['number']).columns
# categorical_columns = df.select_dtypes(exclude=['number']).columns

# option = st.selectbox('Select..', options=['All columns', 'Numerical columns', 'Categorical columns'])

# if option == 'All columns':
#     st.write(df)
# elif option == 'Numerical columns':
#     st.write(df[numerical_columns])
# elif option == 'Categorical columns':
#     st.write(df[categorical_columns])





