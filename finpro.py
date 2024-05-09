import streamlit as st

# Fungsi untuk membuat input per kategori
def input_per_category(category, max_value):
    number_input = st.text_input(f"Masukkan nilai untuk {category}: (1 - {max_value})", key=category)
    return number_input

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

# Mendapatkan input dari pengguna untuk setiap kategori
for category, max_value in categories.items():
    number_input = input_per_category(category, max_value)
    if number_input:
        st.write(f"Nilai yang disimpan untuk {category}: catA_{number_input}")
