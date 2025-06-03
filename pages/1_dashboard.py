import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Judul Halaman
st.title("📊 Halaman 1: Dataset & Visualisasi")

# Path file dari Google Drive (ubah sesuai kebutuhan)
drive_path = '/content/drive/My Drive/data_intro.csv'

# Cek apakah file ada
if os.path.exists(drive_path):
    df = pd.read_csv(drive_path)

    st.subheader("🔍 Dataset")
    st.dataframe(df)

    st.subheader("📌 Statistik Deskriptif")
    st.write(df.describe())

    st.subheader("📈 Korelasi Antar Fitur")
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    except:
        st.warning("Tidak bisa menghitung korelasi karena kolom tidak numerik.")
else:
    st.error(f"File tidak ditemukan di path: {drive_path}")
    st.info("Pastikan Google Drive sudah di-mount di Colab.")

