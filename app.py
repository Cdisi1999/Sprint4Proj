import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.write("Dataset Loaded Successfully:")
st.write(df)

st.header("Vehicle Data Analysis Dashboard")

fig_hist = px.histogram(df, x='price', title='Price Distribution', log=True)
st.plotly_chart(fig_hist)