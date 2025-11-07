# beranda.py
import streamlit as st
import os

def show():
    st.header("Analisis Lendutan")
    st.write("Ini adalah halaman beranda.")
    
    try:
        available_folders = [f for f in os.listdir('.') if os.path.isdir(f)]
    except Exception:
        available_folders = []

    available_folders.insert(0, "-- Pilih Folder --")

    selected = st.selectbox(
        "Daftar Folder:",
        available_folders,
        key="selectbox_beranda"
    )

    if selected != "-- Pilih Folder --":
        st.session_state.selected_folder_home = os.path.abspath(selected)
        st.success(f"Folder '{selected}' dipilih untuk Analisis Lendutan.")
    else:
        st.session_state.selected_folder_home = ""

    st.text_input(
        "Folder yang Dipilih (Beranda):",
        value=st.session_state.selected_folder_home,
        disabled=True
    )