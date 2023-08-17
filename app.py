import pandas as pd
import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder,MinMaxScaler

# adding title to the website
st.title('Price Prediction')

# adding header to the websits - st.header('') for subheader st.subheader('') for text st.text('')


data1= pickle.load(open('C:\\Users\\gskau\\OneDrive\\Desktop\\NIIT\\Practice\\zomato\\app\\data.pkl',"rb"))
data=pd.DataFrame(data1)

online_order_options = ['Yes', 'No']
online_order = st.selectbox('Online Order', online_order_options)

# Options for the "Book Table" selectbox
book_table_options = ['Yes', 'No']
book_table = st.selectbox('Book Table', book_table_options)

#Location Button
Location=st.selectbox('Location',data['location'].unique())

#Cuisines Button
Cuisines=st.selectbox('Cuisines',data['cuisines'].unique())

#Types Button
Types=st.selectbox('Types',data['Types'].unique())

#Slider for rate and votes
Rate=st.slider('Rate',min_value=0.0,max_value=5.0,value=4.5,step=0.1)

Votes=st.slider('Votes',min_value=0,max_value=16832,value=13,step=1)

# Create a dictionary for the new_data
new_data = {
    'online_order': online_order,
    'book_table': book_table,
    'rate': Rate,
    'votes': Votes,
    'location': Location,
    'cuisines': Cuisines,
    'Types': Types
}

# Create a DataFrame from the dictionary
new_data_df = pd.DataFrame([new_data])

for col in ['online_order', 'book_table', 'location', 'cuisines', 'Types']:
    le = LabelEncoder()
    le.fit(data[col])
    new_data_df[col] = le.transform(new_data_df[col])

# Scale numerical features
scaler = MinMaxScaler()
scaler.fit(data[['rate', 'votes']])  # Fit scaler on training data
scaled_numerical_features = scaler.transform(new_data_df[['rate', 'votes']])

# Combine categorical and scaled numerical features
categorical_features = new_data_df.drop(columns=['rate', 'votes'])
scaled_features_df = pd.DataFrame(scaled_numerical_features, columns=['rate', 'votes'])
scaled_new_data = pd.concat([categorical_features, scaled_features_df], axis=1)

# Make sure to use the same order as when you trained the model
column_order = ['online_order', 'book_table','rate', 'votes','location', 'cuisines', 'Types']
scaled_new_data = scaled_new_data[column_order]

#Import Model
model= pickle.load(open('C:\\Users\\gskau\\OneDrive\\Desktop\\NIIT\\Practice\\zomato\\app\\model.pkl',"rb"))
predicted=model.predict(scaled_new_data)


# Creating Button
if st.button('Ok'):
    st.write(predicted)


