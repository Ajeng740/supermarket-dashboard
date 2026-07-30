import streamlit as st
import pandas as pd

df= pd.read_csv("supermarket.csv")

df.columns=df.columns.str.strip()
df.columns=df.columns.str.lower().str.replace(" ","_")

st.title("Supermarket Dashboard")
st.caption("Dashboard analisis penjualan supermarket")

col1, col2=st.columns(2)
col1.metric("Total Sales", f"${df['sales'].sum():,.2f}")
col2.metric("Total Produk", df['product_name'].nunique())

category=st.selectbox("Pilih category", df['category'].unique())
filtered_df = df [df['category']==category]

st.subheader("Top Produk")
top_product = filtered_df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_product)
st.subheader("Sales per Region")
st.bar_chart(df.groupby('region')['sales'].sum())
