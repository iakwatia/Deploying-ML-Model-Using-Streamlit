import streamlit as st
import pandas as pd
import plotly.express as px
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
 


st.set_page_config(
    page_title='Dashboard Page',
    layout='wide'
)

#st.title('Customer Churn Analysis Dashboard')
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

    df = pd.read_csv('./data/clean_data.csv')

    def eda_dashboard():
        st.markdown('### EDA Dashboard')

        col1, col2 = st.columns(2)

        with col1:
            monthlycharges_histogram = px.histogram(df, x='monthlycharges', title= 'Distribution of monthly charges')
            st.plotly_chart(monthlycharges_histogram)

            churn_tenure_box = px.box(df, x='churn', y='tenure', title='Box plot of tenure by churn status', color='churn', points='all')
            st.plotly_chart(churn_tenure_box)

        
        with col2:
            
            churn=px.histogram(df, x=df['churn'], text_auto=True, color=df["churn"], 
                        title=f"Number of customers who churn")
            st.plotly_chart(churn)

            corr_matrix = df.corr(numeric_only=True)
            correlation_matrix=px.imshow(corr_matrix, text_auto=True, width = 1080, height = 500,
                    title= f"correlation matrix")
            st.plotly_chart(correlation_matrix)



    def kpi_dashboard():
        st.markdown('### KPI dashboard')

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
            f"""
            <div style="background-color: #CCE5FF; border-radius: 5px; width: 70%; margin-top: 20px; height:450px;" >
                <h3 style= "margin-left: 30px">Quick Stats About Dataset</h3>
                <hr>
                <h5 style= "margin-left: 30px">Data Size: {df.size}</h5
                <hr>
                <h5 style= "margin-left: 30px"> Churn Rate: {(df['churn'].value_counts
                (normalize=True).get('Yes', 0) * 100):.2f}%.</h5>
                <hr>
                <h5 style = "margin-left: 30px"> Average Monthly Charge:${df['monthlycharges'].mean():.2f}</h5
            </div>
            """,
            unsafe_allow_html=True,
        )
            

            churn_by_contract_bar=px.bar(df, x="contract", color="churn", barmode="group", 
                title="Churn by Contract Type", 
                labels={"contract": "Contract Type", "churn": "Churn"},
                template="plotly", color_discrete_map= {'Yes': 'gold', 'No': 'pink'})
            st.plotly_chart(churn_by_contract_bar)


            churn_paymentmethod_bar=px.bar(df, x="paymentmethod", color="churn", 
                title="Churn by Payment Method",
                labels={"paymentmethod": "Payment Method", "count": "Count", "churn": "Churn"},
                template="plotly", color_discrete_map={'Yes':'brown', 'No':'violet'},barmode="group")
            st.plotly_chart(churn_paymentmethod_bar)

            

        
        
        with col2:

            churn_by_gender_bar=px.bar(df, x="gender", color="churn", barmode="group", 
            title="Churn by Gender", 
            labels={"gender": "Gender", "churn": "Churn"},
            template="plotly", color_discrete_map={'Yes':'red', 'No':'blue'})
            st.plotly_chart(churn_by_gender_bar)


            churn_by_internet=px.bar(df, x="internetservice", color="churn", barmode="group", 
            title="Churn by Internet Service", 
            labels={"internetservice": "Internet Service", "churn": "Churn"},
            template="plotly", color_discrete_map={'Yes':'orange', 'No':'green'})
            st.plotly_chart(churn_by_internet) 
                



    if __name__ == '__main__':
        
        st.title('Dashboard')

        col1, col2 = st.columns(2)
        with col1:
            pass
        with col2:
            st.selectbox('select dashboard type', options=['EDA', 'KPI'], key= 'selected_dashboard_type')

        if st.session_state ['selected_dashboard_type'] =='EDA':
            eda_dashboard()
        else:
            kpi_dashboard()

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