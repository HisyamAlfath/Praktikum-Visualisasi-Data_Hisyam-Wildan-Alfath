# import library yang dibutuhkan
import streamlit as st 
import base64
from PIL import Image

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 3: Data and Media Elements")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("assets/1.jpeg")
# Image Courtesy by unplash
st.write("Sumber Image: Pinterest")

# Image Courtesy
st.write("Displaying Multiple Images")
# Listing out animal images
animal_images = [
    "assets/2.jpeg",
    "assets/3.jpeg",
    "assets/4.jpeg",
    "assets/5.jpeg",
]
# Displaying Multiple Images with width  150
st.image(animal_images, width=150)
st.write("Sumber Image: Pinterest")


# Function to set Image as Background
def add_local_background(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Sumber Image: Pinterest")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
    background-size: cover
    }},
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")
# Calling Image in function
add_local_background("assets/background.jpeg")

original_image = Image.open("assets/6.jpeg")
# Display Original Image
st.title("Original Image")
st.image(original_image)
# Resizing Image to 600x400
resized_image = original_image.resize((400, 300))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)