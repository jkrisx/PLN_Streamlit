import streamlit as st
from modul import beranda, pilih_folder, tentang, sqlite_tab
from utils import *

# Inisialisasi session state di awal
initialize_session_state()

# Judul Aplikasi
st.title("PLN Data Management App")

# Buat tab
tab1, tab2, tab3, tab4 = st.tabs(["1️ AL", "2️ DT", "ℹ️ Tentang", "🛢 SQLite"])

# Isi tab 1 - Biru Muda dengan Border Biru
with tab1:
    beranda.show()

# Isi tab 2 - Ungu Muda dengan Border Ungu
with tab2:
    pilih_folder.show()

# Isi tab 3 - Hijau Muda dengan Border Hijau
with tab3:
    tentang.show()

# Isi tab 4 - Oranye Muda dengan Border Oranye
with tab4:
    sqlite_tab.show()