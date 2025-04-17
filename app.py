touch app.py

import streamlit as st
import pandas as pd

# Title of the app
st.title('My Streamlit App')

# Reading the CSV file (replace with your actual CSV file path)
df = pd.read_csv('/Users/syduluvemula/Desktop/Foundation of Analytics/Exam Part 2/Automobiles.csv'')

# Display the DataFrame
st.write(df)

