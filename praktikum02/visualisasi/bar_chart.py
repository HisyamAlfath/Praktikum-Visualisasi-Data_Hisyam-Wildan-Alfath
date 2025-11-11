import streamlit as st
import pandas as pd
import numpy as np

st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bar Chart")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)