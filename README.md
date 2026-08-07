# Supermarket Sales Dashboard

## Tentang Project

Project ini merupakan dashboard analisis data penjualan supermarket menggunakan Python dan Streamlit.

Project ini dibuat untuk mengolah data transaksi supermarket menjadi informasi yang lebih mudah dipahami. Melalui proses pengolahan data dan visualisasi, pengguna dapat melihat pola penjualan, produk yang memiliki performa terbaik, serta gambaran aktivitas pelanggan.

Project ini dibuat sebagai latihan untuk meningkatkan kemampuan dalam penggunaan Python, analisis data, dan pembuatan dashboard interaktif.

---

## Fitur Dashboard

Dashboard ini memiliki beberapa fitur analisis, yaitu:

### 1. Overview

Menampilkan informasi umum dari data supermarket, seperti:

- Total penjualan
- Jumlah produk
- Jumlah customer
- Tampilan data transaksi


### 2. Sales Analysis

Melakukan analisis penjualan berdasarkan:

- Total sales berdasarkan kategori produk
- Perkembangan penjualan berdasarkan waktu


### 3. Product Analysis

Menampilkan informasi mengenai produk, seperti:

- Produk dengan penjualan tertinggi
- Top 10 produk berdasarkan total sales


### 4. Customer Analysis

Melakukan analisis customer berdasarkan jumlah pembelian untuk mengetahui customer dengan kontribusi penjualan terbesar.

---

## Dataset

Dataset yang digunakan merupakan data transaksi supermarket yang berisi informasi seperti:

- Order ID
- Order Date
- Customer Name
- Category
- Sub Category
- Product Name
- Sales
- Region
- City

Dataset ini digunakan untuk melakukan proses data cleaning, analisis, dan visualisasi.

---

## Teknologi yang Digunakan

- Python
- Pandas
- Matplotlib
- Streamlit
- Git & GitHub

---

## Struktur Project


supermarket-dashboard

│
├── app.py
├── supermarket.csv
├── README.md
└── requirements.txt


---

## Cara Menjalankan Project

### 1. Clone Repository


git clone https://github.com/Ajeng740/supermarket-dashboard.git


### 2. Masuk ke Folder Project


cd supermarket-dashboard


### 3. Install Library yang Dibutuhkan


pip install -r requirements.txt


### 4. Jalankan Dashboard


python -m streamlit run app.py


Dashboard dapat diakses melalui browser:


http://localhost:8501



## Hasil Project

Dashboard ini dapat membantu melihat informasi mengenai:

- Performa penjualan supermarket
- Kategori produk dengan penjualan tertinggi
- Produk yang paling banyak memberikan kontribusi sales
- Customer dengan transaksi terbesar



## Pengembangan Selanjutnya

Project ini masih dapat dikembangkan dengan beberapa fitur tambahan, seperti:

- Customer segmentation menggunakan Machine Learning
- Prediksi penjualan
- Penambahan filter berdasarkan tanggal dan wilayah
- Deployment dashboard secara online



## Author

Ajeng Wijayanti

Project ini dibuat sebagai latihan untuk mengembangkan kemampuan dalam:

- Python Programming
- Data Analysis
- Data Visualization
- Machine Learning