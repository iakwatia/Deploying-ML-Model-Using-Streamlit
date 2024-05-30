# Deploying-ML-Model-Using-Streamlit

# Project Focus: Embedding Machine Learning models into a user-friendly interface such as Streamlit for use by third party stakeholders who don't have the technical knowledge to read a Jupyter notebook.

# In this project, we are going to build an app with the ff:

- Home Page – This will have information about the application including a link to the source code on GitHub and links to all your social handles like GitHub, LinkedIn, Medium, etc.

- Data Page – This page should display the data found in the database shared for this sprint. Connect to a database and make API calls.

- Dashboard Page – Create an interactive dashboard to visualize the data from the database and derive meaningful insights. 

- Predict Page – On this page, the user should interact with the Machine Learning model to make predictions. Predictions should also include probabilities of accuracy.

- History Page -  This page should show a dataframe with your previous predictions made and values entered by users showing as a dataframe.

- Add content to the home page last as it is a finalization of your project and more information page. This should contain information about the app

- On the data page, display a sample for the data from the database, so the users can see the type of data they are working with.

Allow the user to view numeric features 

Allow the user to view categorical features
- On the dashboard page show the visualization based on the analysis you have made using data from the data page. There should be 2 types of dashboard
An EDA dashboard
- KPIs Dashboard
- On the Predict complex page:
Create a form to collect all the fields you need to pass to the model.
Load the model.
Pass the collected data through the model using a custom function.
Display the output and prediction probability. 
Before the user gets access to the app, they have to authenticate their identity. Install streamlit-authenticator for authenticating users of your app.(Simply use a login authentication with nor registration) 
- On the History, you should find a dataframe that contains all predictions that were made, the time the were made and the predicted value including the original input. 

