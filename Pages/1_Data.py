import streamlit as st
import pyodbc 
import pandas as pd

st.set_page_config(
    page_title='Data Page',
    layout='wide'
)

st.title('Telco Customer Churn Database')

@st.cache_resource(show_spinner='connecting to database...')
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets['SERVER']
        + ";DATABASE="
        + st.secrets['DATABASE']
        + ";UID="
        + st.secrets['USERNAME']
        + ";PWD="
        + st.secrets['PASSWORD']

    )

connection = init_connection()

@st.cache_data(show_spinner='running_query...')
def running_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        #st.write(cursor.description)
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])

    return df


def get_all_column():
    sql_query = " SELECT * FROM LP2_Telco_churn_first_3000"
    return running_query(sql_query)

df = get_all_column() 


numerical_columns = df.select_dtypes(include=['number']).columns
categorical_columns = df.select_dtypes(exclude=['number']).columns

option = st.selectbox('Select..', options=['All columns', 'Numerical columns', 'Categorical columns'])

if option == 'All columns':
    st.write(df)
elif option == 'Numerical columns':
    st.write(df[numerical_columns])
elif option == 'Categorical columns':
    st.write(df[categorical_columns])





