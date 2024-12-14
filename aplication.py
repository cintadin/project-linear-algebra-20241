import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import base64

# Konfigurasi halaman harus dipanggil pertama kali
st.set_page_config(
    page_title="Kelompok Project", 
    layout="centered"
    )

# Fungsi untuk mengubah file gambar lokal menjadi Base64
def set_background_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            /* Latar belakang untuk seluruh halaman */
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            /* Sidebar transparansi */
            [data-testid="stSidebar"] {{
                background-color: rgba(255, 255, 255, 0.8); /* Transparansi sidebar */
            }}
            /* Teks styling */
            .title {{
                font-size: 60px;
                color: black; 
                text-align: center;
                font-weight: bold;
                margin-left: auto
                margin-right: auto;
            }}
            .subheader {{
                font-size: 40px;
                color: black;
                text-align: center;
                font-weight: bold;
                margin-left: auto
                margin-right: auto;
                margin-bottom: 0.5px;  /* Mengurangi jarak bawah antara subheader */
            }}
            .content {{
                font-size: 20px;
                color: black;
                text-align: center;
                margin-left: auto
                margin-right: auto;
                margin-top: 0.5px; /* Mengurangi jarak atas antara subheader dan content */
                margin-bottom: 30px;  /* Mengurangi jarak bawah antara baris konten */
            }}
            .logo {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 300px;  /* Ukuran logo yang diperbesar */
                padding-bottom: 40px;  /* Memberikan jarak antara logo dan teks */
            }}
            /* Menambahkan centering untuk seluruh elemen dalam div */
            .container {{
                text-align: center;
                margin-left: auto;
                margin-right: auto;
                max-width: 1500px; /* Menyusun agar konten tidak terlalu lebar */
            }}
            .image-column {{
                text-align: center; /* Memastikan gambar juga berada di tengah */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"File background tidak ditemukan. Periksa path gambar Anda.")

# Atur path file lokal untuk gambar latar belakang
background_image_path = r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\Presiden t1.jpg"
set_background_image(background_image_path)

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        'Project Final Exam',
        ['Introduction', 'Aplication'],
        default_index=0
    )

if select == 'Introduction':
    # Center alignment untuk logo dan teks
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<p class='title'>INTRODUCTION</p>", unsafe_allow_html=True)

    # Logo Kampus, pastikan path logo yang benar
    st.markdown("<img src='data:image/png;base64,{}' class='logo'>".format(base64.b64encode(open("C:\\Users\\Lenovo\\belajar\\LINEAR ALGEBRA\\project group 3\\President_University_Logo.png", "rb").read()).decode()), unsafe_allow_html=True)

    # Info Kelompok
    st.markdown("<p class='subheader'>Group 3 IEN 1 2024</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Chyntia Adinda Ramadani (004202305053)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Ratu Enjelita (004202305032)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Salsabilla Clarysa Putri (004202305016)</p>", unsafe_allow_html=True)

    st.markdown("<p class='subheader'>Program Study</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Industrial Engineering</p>", unsafe_allow_html=True)

    st.markdown("<p class='subheader'>Faculty</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Engineering</p>", unsafe_allow_html=True)

    # Foto Anggota berderet ke samping
    st.markdown("<p class='subheader'>Member Photo</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='image-column'>", unsafe_allow_html=True)
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\cinta2.jpg", caption="Chyntia Adinda,", width=150)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='image-column'>", unsafe_allow_html=True)
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\ratu2.jpg", caption="Ratu Engelita", width=150)
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='image-column'>", unsafe_allow_html=True)
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\salsa2.jpg", caption="Salsabilla Clarysa", width=150)
        st.markdown("</div>", unsafe_allow_html=True)

# Menu "Aplication"
elif select == 'Aplication':
    st.markdown("<p class='title'>Aplication Description</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>This application is used to demonstrate several image transformation techniques such as skewing, rotation, zoom, scaling, resizing, brightness and transparency.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class='subheader'>Image Transformation</p>", unsafe_allow_html=True)
    
    # Upload image
    uploaded_file = st.file_uploader("Upload an image (jpg, png, jpeg)", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)  # Menggunakan Image.open untuk membuka file gambar
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Transformasi gambar
        st.markdown("<p class='subheader'>Choose a Transformation</p>", unsafe_allow_html=True)
        
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Skew", "Zoom", "Scale", "Resize", "Brightness", "Transparency"])
        
        if transformation == "Rotate":
            # Input untuk rotasi (bisa diketik)
            angle_input = st.number_input("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            rotated_image = image.rotate(angle_input)
            st.image(rotated_image, caption="Rotated Image", use_column_width=True)
        
        elif transformation == "Skew":
            # Input untuk skew factor (bisa diketik)
            skew_input = st.number_input("Enter Skew Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            img_array = np.array(image)
            rows, cols = img_array.shape[:2]
            M = np.float32([[1, skew_input, 0], [0, 1, 0]])
            skewed_image = cv2.warpAffine(img_array, M, (cols, rows))
            st.image(skewed_image, caption="Skewed Image", use_column_width=True)
        
        elif transformation == "Zoom":
            # Input untuk zoom factor (bisa diketik)
            zoom_input = st.number_input("Enter Zoom Factor", min_value=1.0, max_value=10.0, value=1.5, step=0.1)
            
            # Zooming dengan memperbesar gambar menggunakan numpy
            img_array = np.array(image)
            height, width = img_array.shape[:2]
            new_height = int(height * zoom_input)
            new_width = int(width * zoom_input)
            
            # Menggunakan cv2 untuk meresize gambar
            zoomed_image = cv2.resize(img_array, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
            st.image(zoomed_image, caption="Zoomed Image", use_column_width=True)
        
        elif transformation == "Scale":
            # Input untuk scale factor (bisa diketik)
            scale_input = st.number_input("Enter Scale Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            width, height = image.size
            scaled_image = image.resize((int(width * scale_input), int(height * scale_input)))
            st.image(scaled_image, caption="Scaled Image", use_column_width=True)
        
        elif transformation == "Resize":
            # Input untuk resize (lebar dan tinggi)
            resize_width_input = st.number_input("Enter New Width", min_value=100, max_value=2000, value=image.width, step=10)
            resize_height_input = st.number_input("Enter New Height", min_value=100, max_value=2000, value=image.height, step=10)
            resized_image = image.resize((resize_width_input, resize_height_input))
            st.image(resized_image, caption="Resized Image", use_column_width=True)

        elif transformation == "Brightness":
            # Pengaturan brightness (slider dan input manual)
            brightness_value = st.slider("Adjust Brightness", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            
            # Memastikan gambar berada dalam mode RGB sebelum diterapkan brightness
            if image.mode != 'RGB':
                image = image.convert('RGB')
                
            # Meningkatkan brightness menggunakan ImageEnhance
            enhancer = ImageEnhance.Brightness(image)
            enhanced_image = enhancer.enhance(brightness_value)  # Terapkan brightness
            st.image(enhanced_image, caption="Brightness Adjusted Image", use_column_width=True)

        elif transformation == "Transparency":
            # Pengaturan transparansi (alpha channel)
            transparency_value = st.slider("Adjust Transparency", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
            
            # Mengubah gambar ke mode RGBA jika belum dalam mode tersebut
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Menyesuaikan tingkat transparansi (alpha channel)
            data = np.array(image)
            data[..., 3] = (data[..., 3] * transparency_value).astype(np.uint8)  # Mengubah nilai alpha
            transparent_image = Image.fromarray(data, 'RGBA')
            
            st.image(transparent_image, caption="Transparency Adjusted Image", use_column_width=True)
