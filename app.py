import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv('vehicles_us.csv')

st.write("Dataset Loaded Successfully:")
st.write(df)

st.header("Vehicle Data Analysis Dashboard")

fig, ax = plt.subplots()
df['price'].hist(ax=ax, bins=35, log=True)
ax.set_title('Price Distribution')
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')

st.pyplot(fig)

fig_1, ax = plt.subplots()
df['model'].value_counts().head(10).plot(kind='bar', ax=ax)
ax.set_title('Top 10 Vehicle Makes')
ax.set_xlabel('Make')
ax.set_ylabel('Count')

st.pyplot(fig_1)

import seaborn as sns

fig_3, ax = plt.subplots()
sns.scatterplot(data=df, x='type', y='price', alpha=0.5, ax=ax)
ax.set_title('Price vs Vehicle Type')
ax.set_xlabel('Vehicle Type')
ax.set_ylabel('Price')
ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

st.pyplot(fig_3)

st.write("Checkbox for Sales of Vehicles")

count_threshold = st.slider(
    "Select # of Vehicles Sold:",
    min_value=500,
    max_value=int(df['model'].value_counts().max()),
    value=500,  # Default value
    step=1
)

filtered_models = df['model'].value_counts()
filtered_models = filtered_models[filtered_models >= count_threshold]

fig_4, ax = plt.subplots()
filtered_models.plot(kind='bar', ax=ax)
ax.set_title('Sales Distribution of Popular Vehicle Models')
ax.set_xlabel('Model')
ax.set_ylabel('Count')

st.pyplot(fig_4)
