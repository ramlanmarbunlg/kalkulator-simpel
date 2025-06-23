import streamlit as st
import math, time

st.title("_Kalkulator_ :blue[Sederhana] :rocket:")

# Definisikan fungsi untuk penjumlahan
def add(x, y):
    return x + y

# Definisikan fungsi untuk pengurangan
def subtract(x, y):
    return x - y

# Definisikan fungsi untuk perkalian
def multiply(x, y):
    return x * y

# Definisikan fungsi untuk pembagian
def divide(x, y):
    if y == 0:
        return "Tidak dapat membagi dengan nol!"
    return x / y

operation = st.selectbox("Pilih operasi", ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"))

num1 = st.number_input("Masukkan angka pertama")
num2 = st.number_input("Masukkan angka kedua")

if operation == "Penjumlahan":
    result = add(num1, num2)
elif operation == "Pengurangan":
    result = subtract(num1, num2)
elif operation == "Perkalian":
    result = multiply(num1, num2)
elif operation == "Pembagian":
    result = divide(num1, num2)

if st.button("Hitung"):
    loading = st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        loading.progress(i+1)
    st.success(f"Hasil: {result}")
  
