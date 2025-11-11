import streamlit as st
import pandas as pd
import numpy as np

st.header("Praktikum 2 Visualisasi Data")
st.subheader("Map")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

df = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078],
    columns=['latitude', 'longitude']
)

st.map(df) 