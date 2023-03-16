import streamlit as st
from PIL import Image

st.set_page_config(
    page_icon='👩‍🏫',
    page_title='Future Study'
)
with st.sidebar:
    header = st.success("Future Study")
    info = st.info("Future Study merupakan representasi skema lanjutan dari penelitian kedepannya")
st.title("Future Study 👩‍🏫")
st.text("Langkah selanjutnya")

container1 = st.container()
with container1:
    col1 = st.columns(1)[0]
    with col1:
        image1 = Image.open('image/flow_future.png')
        st.image(image1, caption='Flow Future', width=400,
                 use_column_width='auto')

st.text("""
    Penelitian ini mengadopsi kerangka kerja CRISP-DM yaitu Cross Industry
    Standard Process for Data Mining dan metode Agile sebagai metode perancangan
    Software. pada penelitian saat ini, bertujuan untuk mrancangan Web Aplikasi
    yang memiliki utilitas menghitung daya arus laut dengan parameter-parameter
    berdasarkan rumus frankle. Hasil saat ini adalah prototype dari Web Aplikasi
    kami yang bernama Ocean Counting Flow Power atau bisa disingkat sebagai OCFLOP.

    Namun, Kedepannya kami akan mengkombinasi dan mengitegerasikan
    Web App ini dengan teknologi IoT dan Data Mining menjadi sebuah sistem 
    terintegrasi melalui perancangan dan pembelajaran, sehingga dapat diimplementasikan
    secara nyata dan memberikan kebermanfaatan, serta kontribusi kepada kepada
    pengembangan ilmu pengetahuan dan bidang energi terbarukan.

    """)
