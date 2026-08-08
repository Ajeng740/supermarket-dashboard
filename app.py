import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(
    page_title="Supermarket Dashboard",
    layout="wide"
)


df = pd.read_csv("supermarket.csv")


df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)


df["order_date"] = pd.to_datetime(
    df["order_date"],
    dayfirst=True,
    errors="coerce"
)

min_date = df["order_date"].min()
max_date = df["order_date"].max()

date_range = st.sidebar.date_input(
    "Pilih Periode",
    value=(min_date, max_date)
)
if len(date_range)==2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    df = df[
        (df["order_date"] >= start_date) &
        (df["order_date"] <= end_date)
    ]
st.title("Supermarket Sales Dashboard")

st.caption(
    "Dashboard untuk melihat data penjualan supermarket"
)


menu = st.sidebar.selectbox(
    "Menu Analisis",
    [
        "Overview",
        "Sales Analysis",
        "Product Analysis",
        "Customer Analysis",
        "Region Analysis"
    ]
)



if menu == "Overview":

    st.subheader("Overview Dashboard")


    total_sales = df["sales"].sum()

    total_order = df["order_id"].nunique()

    total_customer = df["customer_name"].nunique()

    avg_order = df["sales"].sum() / total_order


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )


    col2.metric(
        "Total Orders",
        total_order
    )


    col3.metric(
        "Total Customer",
        total_customer
    )


    col4.metric(
        "Average Order",
        f"${avg_order:,.2f}"
    )


    st.divider()


    st.subheader("Trend Penjualan")


    monthly_sales = (
        df.groupby(
            df["order_date"].dt.to_period("M")
        )["sales"]
        .sum()
    )


    monthly_sales.index = monthly_sales.index.astype(str)


    fig, ax = plt.subplots()


    monthly_sales.plot(
        marker="o",
        ax=ax
    )


    ax.set_xlabel("Bulan")

    ax.set_ylabel("Sales")

    ax.set_title(
        "Sales Trend per Month"
    )


    plt.xticks(rotation=45)


    st.pyplot(fig)


    st.divider()


    st.subheader("Data Preview")


    st.dataframe(
        df.head(10),
        use_container_width=True
    )



elif menu == "Sales Analysis":

    st.subheader(
        "Analisis Penjualan"
    )


    category = st.selectbox(
        "Pilih Category",
        df["category"].unique()
    )


    data_category = df[
        df["category"] == category
    ]


    st.write(
        "Data penjualan berdasarkan category:",
        category
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



    st.subheader(
        "Penjualan berdasarkan Sub Category"
    )


    sub_category_sales = (
        data_category.groupby("sub_category")["sales"]
        .sum()
        .sort_values()
    )


    fig2, ax2 = plt.subplots()


    sub_category_sales.plot(
        kind="bar",
        ax=ax2
    )


    ax2.set_xlabel(
        "Sub Category"
    )


    ax2.set_ylabel(
        "Sales"
    )


    st.pyplot(fig2)



    monthly_sales = (
        df.groupby(
            df["order_date"].dt.month
        )["sales"]
        .sum()
    )


    st.subheader(
        "Trend Penjualan Bulanan"
    )


    fig3, ax3 = plt.subplots()


    monthly_sales.plot(
        marker="o",
        ax=ax3
    )


    ax3.set_xlabel(
        "Bulan"
    )


    ax3.set_ylabel(
        "Sales"
    )


    st.pyplot(fig3)




elif menu == "Product Analysis":

    st.subheader(
        "Analisis Produk"
    )


    top_product = (
        df.groupby("product_name")["sales"]
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
        "Analisis Customer"
    )


    customer = (
        df.groupby("customer_name")["sales"]
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

    st.divider()
    st.subheader(
        "Penjualan berdasarkan segment customer"
    )
    segment_sales = (
        df.groupby("segment")["sales"]
        .sum()
        .sort_values()
    )
    fig2, ax2 = plt.subplots()
    segment_sales.plot(
        kind="bar",
        ax=ax2
    )
    ax2.set_xlabel(
        "Segment"
    )
    ax2.set_ylabel(
        "Sales"
    )
    ax2.set_title(
        "Total Sales berdasarkan Segment Customer"
    )
    st.pyplot(fig2)



elif menu == "Region Analysis":

    st.subheader(
        "Analisis Wilayah"
    )


    region_sales = (
        df.groupby("region")["sales"]
        .sum()
        .sort_values()
    )


    fig, ax = plt.subplots()


    region_sales.plot(
        kind="bar",
        ax=ax
    )


    ax.set_title(
        "Total Sales berdasarkan Region"
    )


    ax.set_xlabel(
        "Region"
    )


    ax.set_ylabel(
        "Sales"
    )


    st.pyplot(fig)
    st.divider()

st.subheader(
    "Top 10 City berdasarkan Sales"
)


city_sales = (
    df.groupby("city")["sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)


fig2, ax2 = plt.subplots()


city_sales.sort_values().plot(
    kind="barh",
    ax=ax2
)


ax2.set_xlabel(
    "Sales"
)


ax2.set_title(
    "Top 10 City berdasarkan Total Sales"
)


st.pyplot(fig2)