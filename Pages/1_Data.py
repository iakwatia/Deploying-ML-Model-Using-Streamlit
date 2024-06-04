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
    pyodbc.connect(
        "DRIVER = {SQL Server}: SERVER="
        + st.secrets['SERVER']
        + "; DATABASE="
        + st.secrets['DATABASE']
        + "; UID="
        + st.secrets['USERNAME']
        + "; PWD="
        + st.secrets['PASSWORD']

    )

connection = init_connection()

@st.cache_data(show_spinner='running_query...')
def running_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        st.write(cursor.description)
        pd.Dataframe.from_records(rows, columns=[column[0] for column in cursor.description])

    return rows

sql_query = " SELECT * FROM LP2_Telco_churn_first_3000"

rows = running_query(sql_query)

st.write(rows)