import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv('vehicles_us.csv')

st.write("Dataset Loaded Successfully:")
st.write(df)

st.header("Vehicle Data Analysis Dashboard")

fig = px.histogram(df, x='price', nbins=35, log_y=True, title='Price Distribution')
fig.update_layout(
    xaxis_title='Price',
    yaxis_title='Frequency'
)

st.plotly_chart(fig)

top_10_makes = df['model'].value_counts().head(10).reset_index()
top_10_makes.columns = ['model', 'count']

fig_1 = px.bar(top_10_makes, x='model', y='count', title='Top 10 Vehicle Makes')
fig_1.update_layout(
    xaxis_title='Make',
    yaxis_title='Count'
)

st.plotly_chart(fig_1)

fig_3 = px.scatter(
    df,
    x='type',
    y='price',
    opacity=0.5,
    title='Price vs Vehicle Type'
)
fig_3.update_layout(
    xaxis_title='Vehicle Type',
    yaxis_title='Price',
    xaxis=dict(tickangle=45)  # Rotate x-axis labels
)
st.plotly_chart(fig_3)

st.write("Checkbox for Sales of Vehicles")

count_threshold = st.slider(
    "Select # of Vehicles Sold:",
    min_value=500,
    max_value=int(df['model'].value_counts().max()),
    value=500,  # Default value
    step=1
)

filtered_models = df['model'].value_counts()
filtered_models = filtered_models[filtered_models >= count_threshold].reset_index()
filtered_models.columns = ['model', 'count']

fig_4 = px.bar(filtered_models, x='model', y='count', title='Sales Distribution of Popular Vehicle Models')
fig_4.update_layout(
    xaxis_title='Model',
    yaxis_title='Count'
)
st.plotly_chart(fig_4)
