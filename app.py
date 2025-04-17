import streamlit as st
import pandas as pd

# Title of the app
st.title('My Streamlit App')

# Reading the CSV file (replace with your actual CSV file path)
df = pd.read_csv('Automobiles.csv')

# Display the DataFrame
st.write(df)

exam1syduluvemula/
├── app.py
└── Automobiles.csv
