import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🏠"
)


def home_page():
    st.write("# Welcome to Ocean Counting Flow Power Web App 🌊")
    st.text('By Student of Pertamina University\n')
    st.sidebar.title("TANKER")
    st.sidebar.success("Choose the Features")

    container1 = st.container()
    with container1:
        col1 = st.columns(1)[0]
        with col1:
            image1 = Image.open('image/flowOceanBali_0.gif')
            st.image(image1, caption='https://peta-maritim.bmkg.go.id/render-static/inaflows/2023/03/2023031300/denpasar/csd_0.gif', width=400,
                     use_column_width='auto')
        st.markdown(
            f"""
            <p>Pembangkit Listrik Tenaga Arus Laut (PLTAL) menjadi salah satu alternatif energi terbarukan yang semakin populer karena ketersediaan energi yang melimpah di laut dan tidak menghasilkan emisi gas rumah kaca.
            Namun, sebelum pemasangan PLTAL dilakukan, perlu dilakukan perhitungan daya arus laut serta evaluasi kelayakan pemasangan. Oleh karena itu, dibutuhkan aplikasi yang dapat mempermudah dan mempercepat penghitungan daya arus laut serta mengevaluasi kelayakan pemasangan PLTAL. Ocean counting flow power (OCFLOP) adalah salah satu aplikasi web yang dibangun untuk tujuan tersebut.<br>
            <br>OCFLOP dibangun menggunakan framework Streamlit yang memungkinkan pembangunan aplikasi web dengan cepat dan mudah. Aplikasi ini dapat diakses melalui web browser tanpa perlu menginstal software atau memerlukan pengetahuan pemrograman yang mendalam. Dengan menggunakan OCFLOP, pengguna dapat memasukkan data seperti kecepatan arus, kerapatan air laut, dan luas daerah penampang turbin, dan kemudian aplikasi akan menghitung daya arus laut serta mengevaluasi kelayakan pemasangan PLTAL di daerah tersebut</p>
             
            
            """, unsafe_allow_html=True
        )
        # st.subheader("Tujuan")
        # st.markdown(f"""
        #     Tujuan yang diharapkan dari karya cipta teknologi ini adalah sebagai berikut<br> 

        # """, unsafe_allow_html=True)

        # st.subheader("Manfaat")
        # st.markdown(f"""
        # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat massa vel velit consequat, quis convallis risus venenatis.
        # Phasellus mattis vestibulum est ac feugiat. Sed consequat, quam a lacinia bibendum, eros orci tincidunt metus, vitae tincidunt mi dolor sit amet magna. Vivamus vitae velit gravida, eleifend mi a, finibus nibh. Donec mollis auctor elit, vel tristique sapien bibendum ut. Sed eu massa purus. Sed ac sapien dui.""")


if __name__ == "__main__":
    home_page()
