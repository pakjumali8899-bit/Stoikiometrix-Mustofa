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
        # 1. Inisialisasi menu halaman di dalam dashboard (jika belum ada)
    if 'menu_aktif' not in st.session_state:
        st.session_state.menu_aktif = 'dashboard'
    
    # ==========================================
    # KONDISI A: JIKA DI DASHBOARD UTAMA
    # ==========================================
    if st.session_state.menu_aktif == 'dashboard':
        st.title("Dashboard Pembelajaran 📊")
        st.write("Pilih level tantanganmu di bawah ini:")
        
        # Kotak Level 1
        with st.container(border=True):
            st.subheader("🟢 Level 1: Hukum Dasar Kimia")
            st.write("Pelajari pondasi utama stoikiometri: Hukum Lavoisier & Proust.")
            if st.button("Mulai Belajar Level 1 🚀"):
                st.session_state.menu_aktif = 'level_1'
                st.rerun()
                
        # Kotak Level 2 (Terkunci)
        with st.container(border=True):
            st.subheader("🔒 Level 2: Stoikiometri Senyawa")
            st.caption("Terkunci (Selesaikan Level 1 dengan nilai ≥ 70)")
            st.button("Mulai Level 2 🎯", disabled=True)
            
        # Kotak Level 3 (Terkunci)
        with st.container(border=True):
            st.subheader("🔒 Level 3: Stoikiometri Reaksi")
            st.caption("Terkunci (Selesaikan Level 2 dulu)")
            st.button("Mulai Level 3 ⚔️", disabled=True)
            
    # ==========================================
    # KONDISI B: JIKA SISWA MASUK KE LEVEL 1
    # ==========================================
    elif st.session_state.menu_aktif == 'level_1':
        if st.button("⬅️ Kembali ke Dashboard"):
            st.session_state.menu_aktif = 'dashboard'
            st.rerun()
            
        st.title("🧪 Level 1: Hukum Dasar Kimia")
        st.write("Pondasi awal sudah siap! Di langkah berikutnya, kita akan isi materi lengkap dan kuisnya di sini.")

    # ==========================================
    # TOMBOL LOGOUT (Selalu di paling bawah)
    # ==========================================
    st.write("---")
    if st.button("Keluar / Logout"):
        st.session_state.sudah_login = False
        st.session_state.username = ""
        if 'menu_aktif' in st.session_state:
            del st.session_state.menu_aktif
        st.rerun()
        
