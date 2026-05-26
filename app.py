import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Data ---
df = pd.read_csv('car_wash.csv')
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

# --- Title ---
st.title('🚗 Car Wash Sales Dashboard')
st.write('Interactive sales analysis for the business')

# --- Summary Numbers ---
col1, col2, col3 = st.columns(3)
col1.metric('Total Revenue', f"RM {df['price'].sum():,.2f}")
col2.metric('Total Transactions', len(df))
col3.metric('Average Sale', f"RM {df['price'].mean():,.2f}")

# --- Chart 1: Monthly Revenue ---
st.subheader('Monthly Revenue')
monthly = df.groupby('month')['price'].sum()
fig1, ax1 = plt.subplots(figsize=(10, 4))
monthly.plot(kind='line', ax=ax1, color='steelblue', marker='o')
ax1.set_ylabel('Revenue (RM)')
ax1.set_xlabel('Month')
st.pyplot(fig1)

# --- Chart 2: Top Services ---
st.subheader('Revenue by Service Type')
service_rev = df.groupby('service_type')['price'].sum().sort_values()
fig2, ax2 = plt.subplots(figsize=(8, 4))
service_rev.plot(kind='barh', ax=ax2, color='coral')
ax2.set_xlabel('Revenue (RM)')
st.pyplot(fig2)

# --- Chart 3: Payment Methods ---
st.subheader('Payment Methods')
fig3, ax3 = plt.subplots(figsize=(6, 6))
df['payment_method'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax3)
ax3.set_ylabel('')
st.pyplot(fig3)

# --- Raw Data Toggle ---
if st.checkbox('Show raw data'):
    st.dataframe(df)