# import library yang dibutuhkan
import streamlit as st

st.header("Praktikum 3 Visualisasi Data")
st.subheader("Bagian 1: Teks Element")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

st.write("Hello")
st.write('World!!!!')

st.write('World!!!!')
st.title("This is our Title")
st.header("""This is our Header""")
st.subheader("""This is our Sub-header""")
st.caption("""This is our Caption""")

# Displaying Plain Text
st.text("Hi,\nPeople\t!!!!!!!!!!")
st.text('Welcome to')
st.text(""" Streamlit's World""")

# Displaying Markdown
st.markdown("# Hi,\n# ***People*** \t!!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

# Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex(r"""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
        + \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
    public static void main(String args[]) {
        System.out.println("Hello World");
    }
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code("""<p id="demo"></p>
<script>
try {
    addlert("Welcome guest!");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script> """)



# Praktikum Dikelas
# text element
st.header("Displaying Text Element")
st.header("Ini header") # untuk membuat tulisan header
st.subheader("Ini sub header") # untuk
st.text("Ini teks biasa tanpa format")
st.markdown("**ini teks bold** dan *ini teks italic*")
st.markdown("""
- ini baris 1
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris
""")

st.caption("Ini caption") # teks kecil dibawah elemen 
st.title("Ini Judul")

# coba mandiri
# tuliskan:
# 1. judul praktikum pakai title() = Praktikum 1 Visualisasi Data
st.title("Praktikum 1 Visualisasi Data")
# 2. bagian praktikum pakai subheader() = Bagian 1: Text Element
st.subheader("Bagian 1: Text Element")
# 3. nama lengkap anggota - nim pakai markdown multibaris """
st.markdown("""
1. Fatih Mubasyir
- 0110222186
2. Hisyam Wildan Alfath
- 0110222206
3. Dean Pramona
- 0110122163
""")

# Bagian 2: 
st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') # rumus kuadrat binominal

# Bagian 3: Menampilkan Kode Program
st.header("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello():
    print("Hello, Streamlit!)
'''

# st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main(String arg[]) {
            System.out.printIn("Hello World!);
        }
    }
""", language='java')
# Fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti Java, JavaScript, C++, HTML, dll

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert ("Welcome guestl); // kesalahan ketik (addalaert) sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
# Kode ini menunjukkan contoh bågaimana menangani error (exception) di JavaScript.
# Hasilnya tidak dijalankan di Streamlit, tapi ditampilkan sebagai contoh kode.