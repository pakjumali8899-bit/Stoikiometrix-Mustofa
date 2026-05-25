import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Stoikiometrix Mustofa", page_icon="🧪")

# --- SESSION STATE UNTUK BAHASA & LOGIN ---
# Ini fungsi agar web ingat pilihan bahasa dan status login siswa
if 'bahasa' not in st.session_state:
    st.session_state.bahasa = 'ID'
if 'sudah_login' not in st.session_state:
    st.session_state.sudah_login = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# --- FUNGSI GANTI BAHASA ---
def ganti_bahasa():
    if st.session_state.bahasa == 'ID':
        st.session_state.bahasa = 'EN'
    else:
        st.session_state.bahasa = 'ID'

# Tombol ganti bahasa di pojok
st.button("🌐 ID / EN", on_click=ganti_bahasa)

# --- KAMUS BAHASA ---
teks = {
    'ID': {
        'judul': "Selamat Datang di Stoikiometrix Mustofa! 🧪",
        'subjudul': "Silakan login untuk memulai petualangan belajarmu.",
        'user': "Nama Pengguna (Username)",
        'pass': "Kata Sandi",
        'masuk': "Masuk",
        'berhasil': "Login berhasil! Selamat belajar, ",
        'salah': "Username atau password tidak boleh kosong!"
    },
    'EN': {
        'judul': "Welcome to Stoikiometrix Mustofa! 🧪",
        'subjudul': "Please login to start your learning adventure.",
        'user': "Username",
        'pass': "Password",
        'masuk': "Login",
        'berhasil': "Login successful! Happy learning, ",
        'salah': "Username or password cannot be empty!"
    }
}

lang = st.session_state.bahasa

# --- HALAMAN LOGIN ---
if not st.session_state.sudah_login:
    st.title(teks[lang]['judul'])
    st.write(teks[lang]['subjudul'])
    
    # Kolom input
    username = st.text_input(teks[lang]['user'])
    password = st.text_input(teks[lang]['pass'], type="password")
    
    # Logika jika tombol masuk ditekan
    if st.button(teks[lang]['masuk']):
        if username and password:
            st.session_state.sudah_login = True
            st.session_state.username = username
            st.rerun() # Refresh halaman setelah login
        else:
            st.error(teks[lang]['salah'])

# --- HALAMAN UTAMA (JIKA SUDAH LOGIN) ---
else:
    st.success(f"{teks[lang]['berhasil']} {st.session_state.username}! 🎉")
    st.write("Di sini nanti kita akan taruh Level 1: Hukum Dasar Kimia.")
    
    # Tombol keluar (Logout)
    if st.button("Keluar / Logout"):
        st.session_state.sudah_login = False
        st.session_state.username = ""
        st.rerun()
      
