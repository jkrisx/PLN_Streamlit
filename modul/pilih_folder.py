# pilih_folder.py
import streamlit as st
from utils import get_available_folders

def show():
    st.header("Pilih Folder")
    st.write("Pilih folder dari daftar folder yang tersedia.")

    available_folders = get_available_folders('.')
    available_folders.insert(0, "-- Pilih Folder --")

    selected = st.selectbox(
        "Daftar Folder:",
        available_folders,
        key="selectbox_pilih_folder"
    )

    if selected != "-- Pilih Folder --":
        st.session_state.selected_folder_dt = selected  # atau os.path.abspath(selected) jika perlu path penuh
        st.success(f"Folder '{selected}' dipilih untuk Data Tabel.")
    else:
        st.session_state.selected_folder_dt = ""

    st.text_input(
        "Folder yang Dipilih (DT):",
        value=st.session_state.selected_folder_dt,
        disabled=True
    )