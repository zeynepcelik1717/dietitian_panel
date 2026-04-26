import streamlit as st
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
supabase = create_client(os.getenv("supabase_url"), os.getenv("supabase_key"))

st.set_page_config(page_title="Diyetisyen Paneli", page_icon="🥗")
st.title("Diyetisyen Yönetim Paneli")
st.write("MVP geliştiriliyor....")
st.info("Bu Proje 14 Haziran 2026 da hazır olacak")

try:
    result = supabase.table("danisanlar").select("*").limit(1).execute()
    st.success("SUPABASE BAĞLANTISI BAŞARILI")
except Exception as e:
    st.error(f"Bağlantı hatası: {e}")