import pickle
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import openpyxl
from openpyxl.styles import Font, PatternFill
import tempfile

# User Authentication
names = ["TI Polda NF 1", "TI Polda NF 2"]
usernames = ["admin1", "admin2"]

# load hashed kd_akses
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_kd_akses = pickle.load(file)

authenticator = stauth.Authenticate(
    names, usernames, hashed_kd_akses, "lookup", "abcdef")
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/kode akses salah")

if authentication_status == None:
    st.warning("Silahkan masukan username dan kode akses")

url = "https://osmanlokpts.streamlit.app/"
url_panduan = "https://docs.google.com/document/d/1zc9W_Tt51J9POZaybez1KBVbNWhpEiRsGsfo5VsRQJI/edit?usp=sharing"

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    with st.sidebar:
        # Tombol untuk URL utama dengan warna GreenYellow
        st.markdown(f'''
<a href="{url}"><button style="background-color:GreenYellow; border:none; color:white; padding:10px 24px; text-align:center; display:inline-block; font-size:16px; margin:4px 2px; cursor:pointer;">Report Lokasi</button></a>
''', unsafe_allow_html=True)

        # Tombol untuk URL panduan dengan warna Tomato
        st.markdown(f'''
<a href="{url_panduan}"><button style="background-color:Tomato; border:none; color:white; padding:10px 24px; text-align:center; display:inline-block; font-size:16px; margin:4px 2px; cursor:pointer;">Panduan v. 1.0</button></a>
''', unsafe_allow_html=True)

        # Pilihan file
        selected_file = option_menu(
            menu_title="Pilih file:",
            options=["Pivot",
                     "Nilai Std. SD (K13), SMP (K13-KM), 10 SMA (KM)",
                     "Nilai Std. 8 SMP (KM)",
                     "Nilai Std. SD (KM)",
                     "Nilai Std. 10, 11 IPS (K13)",
                     "Nilai Std. 11 SMA (KM)",
                     "Nilai Std. 10, 11, PPLS IPA",
                     "Nilai Std. PPLS IPS"],
        )

    # k13
    k13_4sd_mat = ''
    k13_4sd_ind = ''
    k13_4sd_eng = ''
    k13_4sd_ipa = ''
    k13_4sd_ips = ''
    k13_5sd_mat = ''
    k13_5sd_ind = ''
    k13_5sd_eng = ''
    k13_5sd_ipa = ''
    k13_5sd_ips = ''
    k13_6sd_mat = ''
    k13_6sd_ind = ''
    k13_6sd_eng = ''
    k13_6sd_ipa = ''
    k13_6sd_ips = ''
    k13_7smp_mat = ''
    k13_7smp_ind = ''
    k13_7smp_eng = ''
    k13_7smp_ipa = ''
    k13_7smp_ips = ''
    k13_8smp_mat = ''
    k13_8smp_ind = ''
    k13_8smp_eng = ''
    k13_8smp_ipa = ''
    k13_8smp_ips = ''
    k13_9smp_mat = ''
    k13_9smp_ind = ''
    k13_9smp_eng = ''
    k13_9smp_ipa = ''
    k13_9smp_ips = ''
    k13_10ipa_mat = ''
    k13_10ipa_bio = ''
    k13_10ipa_fis = ''
    k13_10ipa_kim = ''
    k13_10ips_mat = ''
    k13_10ips_ind = ''
    k13_10ips_eng = ''
    k13_10ips_sej = ''
    k13_10ips_eko = ''
    k13_10ips_sos = ''
    k13_10ips_geo = ''
    k13_11ipa_mat = ''
    k13_11ipa_bio = ''
    k13_11ipa_fis = ''
    k13_11ipa_kim = ''
    k13_11ips_mat = ''
    k13_11ips_ind = ''
    k13_11ips_eng = ''
    k13_11ips_sej = ''
    k13_11ips_eko = ''
    k13_11ips_sos = ''
    k13_11ips_geo = ''

    # km
    km_4sd_mat = ''
    km_4sd_ind = ''
    km_4sd_eng = ''
    km_4sd_ipas = ''
    km_5sd_mat = ''
    km_5sd_ind = ''
    km_5sd_eng = ''
    km_5sd_ipas = ''
    km_6sd_mat = ''
    km_6sd_ind = ''
    km_6sd_eng = ''
    km_6sd_ipa = ''
    km_6sd_ips = ''
    km_7smp_mat = ''
    km_7smp_ind = ''
    km_7smp_eng = ''
    km_7smp_ipa = ''
    km_7smp_ips = ''
    km_8smp_mat = ''
    km_8smp_mat_sb = ''
    km_8smp_ind = ''
    km_8smp_eng = ''
    km_8smp_ipa = ''
    km_8smp_ips = ''
    km_9smp_mat = ''
    km_9smp_ind = ''
    km_9smp_eng = ''
    km_9smp_ipa = ''
    km_9smp_ips = ''
    km_10sma_mat = ''
    km_10sma_ind = ''
    km_10sma_eng = ''
    km_10sma_ipa = ''
    km_10sma_ips = ''
    km_11sma_mat_1 = ''
    km_11sma_mat_2 = ''
    km_11sma_ind = ''
    km_11sma_eng = ''
    km_11sma_sej = ''
    km_11sma_eko = ''
    km_11sma_sos = ''
    km_11sma_geo = ''
    km_11sma_ant = ''
    km_11sma_bio = ''
    km_11sma_fis = ''
    km_11sma_kim_1 = ''
    km_11sma_kim_2 = ''

    # ppls
    ppls_ipa_mat = ''
    ppls_ipa_bio = ''
    ppls_ipa_fis = ''
    ppls_ipa_kim = ''
    ppls_ips_geo = ''
    ppls_ips_eko = ''
    ppls_ips_sej = ''
    ppls_ips_sos = ''
