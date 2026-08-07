import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("supermarket.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)


df["order_date"] = pd.to_datetime(
    df["order_date"],
    dayfirst=True,
    errors="coerce"
)


st.title("🛒 Supermarket Sales Analytics Dashboard")

st.caption(
    "Dashboard analisis penjualan supermarket menggunakan Python & Streamlit"
)


menu = st.sidebar.selectbox(
    "Menu Analisis",
    [
        "Overview",
        "Sales Analysis",
        "Product Analysis",
        "Customer Analysis"
    ]
)


if menu == "Overview":

    st.subheader(" Overview Data")


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Total Sales",
        f"${df['sales'].sum():,.2f}"
    )


    col2.metric(
        "Total Produk",
        df["product_name"].nunique()
    )


    col3.metric(
        "Total Customer",
        df["customer_name"].nunique()
    )


    st.write("Preview Data")

    st.dataframe(
        df.head(10)
    )


elif menu == "Sales Analysis":


    st.subheader(
        " Analisis Penjualan"
    )


    category_sales = (
        df.groupby("category")["sales"]
        .sum()
        .sort_values()
    )


    fig, ax = plt.subplots()

    category_sales.plot(
        kind="bar",
        ax=ax
    )


    ax.set_title(
        "Total Sales berdasarkan Category"
    )

    ax.set_xlabel(
        "Category"
    )

    ax.set_ylabel(
        "Sales"
    )


    st.pyplot(fig)


    monthly_sales = (
        df.groupby(
            df["order_date"].dt.month
        )["sales"]
        .sum()
    )


    st.subheader(
        "Trend Penjualan Bulanan"
    )


    fig2, ax2 = plt.subplots()


    monthly_sales.plot(
        marker="o",
        ax=ax2
    )


    ax2.set_xlabel(
        "Bulan"
    )

    ax2.set_ylabel(
        "Sales"
    )


    st.pyplot(fig2)


elif menu == "Product Analysis":


    st.subheader(
        " Analisis Produk"
    )


    top_product = (
        df.groupby("product_name")
        ["sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )


    st.write(
        "Top 10 Produk berdasarkan Sales"
    )


    fig, ax = plt.subplots()


    top_product.sort_values().plot(
        kind="barh",
        ax=ax
    )


    ax.set_xlabel(
        "Sales"
    )


    st.pyplot(fig)



elif menu == "Customer Analysis":


    st.subheader(
        " Analisis Customer"
    )


    customer = (
        df.groupby("customer_name")
        ["sales"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )


    st.write(
        "Top 10 Customer berdasarkan pembelian"
    )


    st.dataframe(
        customer
    )


    fig, ax = plt.subplots()


    customer.sort_values().plot(
        kind="barh",
        ax=ax
    )


    ax.set_xlabel(
        "Total Sales"
    )


    st.pyplot(fig)