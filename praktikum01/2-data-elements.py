# import library yang dibutuhkan
import streamlit as st
import pandas as pd         # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np          # untuk membuat data numerik acak
import altair as alt        # untuk membuat chart interaktif
import matplotlib.pyplot as plt

st.header("Praktikum 3 Visualisasi Data")
st.subheader("Bagian 2: Data Elements")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

# Dataframe
# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
st.dataframe(df)

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

# Table
# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
# defining data in table
st.table(df)

# Metrics
# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

# Defining Colums
c1, c2, c3 = st.columns(3)
#Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

# The write( ) Function as a Superfunction
df = pd.DataFrame(
np.random.randn(30, 10),
columns=('col_no %d' % i for i in range(10)))
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])
# Defining Chart in write() function
st.write(chart)

# Magic
# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4
# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""
# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

# Magic working on Chart
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart

# Praktikum di kelas
# Memampilkan judul
st.title("Praktikum 1 Visualisasi Data")
st.caption("Bagian 1: Text Element")

# 3. nama lengkap anggota - nim pakai markdown multibaris """
st.markdown("""
Kelompok 7:
- Dean Pramona - 0110122163
- Fatih Mubasyir - 0110222186
- Hisyam Wildan Alfath - 0110222206
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan dataframe
st.dataframe(df)

# Highlight Nilai Minimum
st.subheader("Highlight Minimum Value di DataFrame")

# Highlight nilai terkecil disetiap kolom dataframe
# axix=0 berkerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# Menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka penting
st.subheader("Metrics")
# Menampilkan metrik tunggal
st.metric(label="Temperature", value="31 C", delta="1.2 C") # Kenaikan 1.2 C

# Metrics sesuai delta_color
# delta_color digunakan 

# definisikan variabel metrics
col1, col2, col3 = st.columns(3)

# Menampilam indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10,
delta_color="off") # netral (tidak baik, tidak buruk)

# Menampilkan metrik tämbahan dengan nilai kosong atau nol 
st.metric(label="Speed", value=None, delta=0) # kosong # naik karena di setting default
st.metric ("Trees", "91456", "-1132649") # penurunan
