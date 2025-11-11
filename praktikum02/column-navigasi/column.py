import streamlit as st

st.header("Praktikum 2 Visualisasi Data")
st.subheader("Column Navigasi")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../assets/contoh.jpeg", caption="Gambar 1")
col2.write("Ini adalah kolom kedua")
col2.image("../../praktikum01/assets/1.jpeg", caption="Gambar 2")