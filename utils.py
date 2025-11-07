import streamlit as st
import os


def get_available_folders(path='.'):
    """Mengambil daftar folder di path tertentu."""
    try:
        return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    except FileNotFoundError:
        st.error(f"Direktori '{path}' tidak ditemukan.")
        return []

def initialize_session_state():
    """Inisialisasi semua session_state yang dibutuhkan."""
    if 'selected_folder_home' not in st.session_state:
        st.session_state.selected_folder_home = ""
    if 'selected_folder_dt' not in st.session_state:
        st.session_state.selected_folder_dt = ""