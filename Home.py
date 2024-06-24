import streamlit as st
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

st.set_page_config(
    page_title='Home Page',
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

    st.title('Customer Churn Prediction')
    
    # Home Page Content
    st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
    st.markdown("""
            <div class="slide-in-left-animation">
                <p>The <span class="slide-in-bottom-animation">Customer Churn Prediction App</span> is designed to help businesses in the telecommunications industry predict whether a customer is likely to churn (leave the service). By leveraging machine learning techniques, this app provides valuable insights into customer behavior, allowing companies to take proactive measures to improve customer retention.</p>
            </div>
        """, unsafe_allow_html=True)
    
        # Create columns for Key Features, How It Works, and Benefits
    col1, col2, col3 = st.columns(3)
    
        # Key Features with slide-in-right animation
    with col1:
        st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
        st.markdown("## Key Features")
        st.markdown("""
        - **Model Training:** Train various machine learning models, such as Logistic Regression, Random Forest, and XGBoost, to predict customer churn.
        - **Feature Importance:** Analyze feature importances to understand the drivers of customer churn.
        - **User-Friendly Interface:** Interact with the app through an intuitive and engaging user interface.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # How It Works with slide-in-bottom animation
    with col2:
        st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
        st.markdown("## How It Works")
        st.markdown("""
        1. **Data Collection:** Gather customer data from various sources.
        2. **Data Preprocessing:** Clean and preprocess the data for model training.
        3. **Model Training:** Train multiple machine learning models to predict churn.
        4. **Model Evaluation:** Evaluate model performance using various metrics.
        5. **Deployment:** Deploy the best-performing model to make real-time predictions.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Benefits with slide-in-top animation
    with col3:
        st.markdown('<div class="slide-in-top-animation">', unsafe_allow_html=True)
        st.markdown("## Benefits")
        st.markdown("""
        - **Improve Customer Retention:** Identify at-risk customers and take proactive measures to retain them.
        - **Optimize Marketing Strategies:** Tailor marketing efforts to target customers who are likely to churn.
        - **Enhance Business Performance:** Reduce churn rates and increase customer lifetime value.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        ---
        © 2024 Customer Churn Prediction Project. All rights reserved.
    """)
    
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
 
