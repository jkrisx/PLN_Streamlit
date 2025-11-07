import streamlit as st
import sqlite3
import pandas as pd
import tempfile
import os

def show():
    st.header("Baca File SQLite")
    st.write("Pilih file SQLite untuk dibaca.")

    uploaded_file = st.file_uploader("Upload file SQLite", type=["db", "sqlite", "sqlite3"])

    if uploaded_file is not None:
        try:
            # Simpan file yang diupload ke temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp_file:
                tmp_file.write(uploaded_file.read())
                temp_db_path = tmp_file.name

            # Koneksi ke database SQLite
            conn = sqlite3.connect(temp_db_path)

            # Ambil daftar tabel
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]

            if table_names:
                selected_table = st.selectbox("Pilih Tabel", table_names)

                if selected_table:
                    query = f"SELECT * FROM {selected_table};"
                    df = pd.read_sql_query(query, conn)
                    st.write(f"Isi Tabel: {selected_table}")
                    st.dataframe(df)
            else:
                st.warning("Tidak ada tabel ditemukan di database.")

            conn.close()

            # Hapus file sementara
            os.unlink(temp_db_path)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca database: {e}")
    else:
        st.info("Silakan upload file SQLite (.db, .sqlite, .sqlite3)")