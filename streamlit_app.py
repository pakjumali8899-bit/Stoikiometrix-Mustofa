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
                # --- INISIALISASI VARIABEL KUNCI LEVEL ---
        if 'level_2_terbuka' not in st.session_state:
            st.session_state.level_2_terbuka = False

        # --- MEMBUAT TAB INTERAKTIF AGAR TIDAK FLAT ---
        tab1, tab2, tab3 = st.tabs(["📝 Materi Lengkap", "🎛️ Simulasi Lab", "✍️ Kuis Level 1"])
        
        # --- TAB 1: MATERI ---
        with tab1:
            st.header("1. Hukum Kekekalan Massa (Lavoisier)")
            st.info("💡 **Inti Teori:** Antoine Lavoisier (1789) menemukan bahwa dalam sistem tertutup, **massa total zat sebelum reaksi sama dengan massa total zat setelah reaksi.**")
            st.write("### Persamaan Reaksi Kimia Sempurna (Format LaTeX):")
            st.latex(r"\text{C}_{(s)} + \text{O}_{2(g)} \rightarrow \text{CO}_{2(g)}")
            st.latex(r"\text{Massa Karbon (12g)} + \text{Massa Oksigen (32g)} = \text{Massa Karbon Dioksida (44g)}")
            
            st.write("---")
            st.header("2. Hukum Perbandingan Tetap (Proust)")
            st.info("💡 **Inti Teori:** Joseph Proust (1799) menyatakan bahwa **perbandingan massa unsur-unsur dalam suatu senyawa adalah selalu tetap dan tertentu.**")
            st.write("### Contoh Reaksi Pembentukan Air:")
            st.latex(r"2\text{H}_{2(g)} + \text{O}_{2(g)} \rightarrow 2\text{H}_2\text{O}_{(l)}")
            st.write("Perbandingan massa Hidrogen dan Oksigen untuk membentuk air selalu **1 : 8**.")

        # --- TAB 2: SIMULASI INTERAKTIF ---
        with tab2:
            st.header("🎛️ Laboratorium Virtual Mini")
            st.write("Geser tombol di bawah untuk menentukan massa zat pereaksi, lalu lihat apakah Hukum Lavoisier terbukti secara otomatis!")
            
            massa_a = st.slider("Masukkan Massa Zat A (gram)", 1.0, 50.0, 10.0, step=0.5)
            massa_b = st.slider("Masukkan Massa Zat B (gram)", 1.0, 50.0, 20.0, step=0.5)
            
            st.metric(label="Massa Total Sebelum & Sesudah Reaksi", value=f"{massa_a + massa_b} gram")
            st.success("✅ Terbukti! Massa total zat sebelum dan sesudah reaksi nilainya sama sesuai Hukum Lavoisier.")

        # --- TAB 3: KUIS EVALUASI ---
        with tab3:
            st.header("✍️ Evaluasi Pemahaman Level 1")
            st.write("Selesaikan kuis di bawah ini untuk membuka kunci Level 2!")
            
            soal1 = st.radio(
                "Soal 1: Jika 5 gram besi direaksikan dengan 3 gram belerang dalam wadah tertutup rapat, berapakah massa besi belerang yang dihasilkan?",
                ["3 gram", "5 gram", "8 gram", "15 gram"],
                key="kuis_s1"
            )
            
            if st.button("Kirim Jawaban 📝"):
                if soal1 == "8 gram":
                    st.session_state.level_2_terbuka = True
                    st.balloons() # Efek animasi balon resmi Streamlit
                    st.success("🎉 Selamat! Jawabanmu benar (Nilai: 100/100). Kunci Level 2 sekarang sudah TERBUKA!")
                else:
                    st.error("❌ Jawabanmu masih kurang tepat. Silakan baca kembali materi di Tab 1 dan coba lagi!")
                    
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
        
