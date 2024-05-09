import streamlit as st

# Dictionary yang berisi jumlah kategori untuk setiap kategori
categories = {
    'categoryA': 167,
    'categoryB': 2,
    'categoryC': 2212,
    'categoryD': 3,
    'categoryE': 25,
    'categoryF': 3,
    'unit': 19
}

# Mendapatkan input dari pengguna
selected_category = st.selectbox("Pilih Kategori:", list(categories.keys()))
number_input = st.text_input("Masukkan Nomor:")

# Mengonversi nomor ke format yang diinginkan
if number_input:
    selected_value = f"{selected_category}_catA_{number_input}"
    st.write("Nilai yang disimpan:", selected_value)
else:
    st.write("Masukkan nomor untuk mendapatkan nilai yang disimpan")
