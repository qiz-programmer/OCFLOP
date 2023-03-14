import streamlit as st
import numpy as np
import pandas as pd

# Title
st.markdown("# Help ❓")
st.text('By Student of Pertamina University\n')
# Sidebar

# contain
st.subheader("Cara Menggunakan ")
st.subheader("Measurement")
st.markdown('''Cara menggunakan WEB APP penghitung daya arus laut adalah sebagai berikut

Langkah-langkah:
* Buka sidebar. 
* Pilih  fitur measurement.
* pilih opsi perhitungan pada selectbox 
* Masukan data lapangan sesuai parameter inputan.
* Tekan button "Hitung"
*

Hasil kalkulasi akan muncul pada main page measurement dalam bentuk metric. Terdapat 3 metric yang menunjukan 
hasil daya arus laut dan parameter inputan adalah sebagai berikut. 
1. Metric yang menunjukan daya arus laut
2. Kecepatan arus laut
3. Efisiensi turbin

Sedangkan untuk luas penampang turbin memiliki luaran metric, sebagai berikut.
1. Metric Luas Penampang Turbin
2. Daya arus laut
3. kecepatan arus
''')
st.subheader("Fitur Show Data")
st.markdown("""
Fitur Show data merupakan fitur yang menampilkan data kecepatan arus, di mana parameter ini merupakan parameter utama dalam perhitungan daya arus laut.
fitur ini menyediakan data arus laut secara real time sesuai waktu UTC dengan selisih waktu 3 jam. 
Data ini ini diambil berdasarkan data BMKG OFS atau Badan Meteorologi Klimatologi dan Geofisika Ocean Forecast System yang khusus menyediakan data kemaritiman di Indonesia.
""")



