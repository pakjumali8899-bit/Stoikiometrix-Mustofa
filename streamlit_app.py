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
    elif st.session_state.menu_aktif == 'dashboard':

    
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
        
        if 'level_2_terbuka' not in st.session_state:
            st.session_state.level_2_terbuka = False

        tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 1"])

        # ======================================================================
        # TAB 1: MATERI LENGKAP (5 HUKUM) DENGAN LATEX SEMPURNA
        # ======================================================================
        with tab_materi:
            st.write("Selesaikan membaca seluruh materi dan tantangan latihan di bawah ini sebelum maju ke Kuis Akhir!")
            st.write("---")

            # --- 1. LAVOISIER ---
            st.subheader("1. Hukum Kekekalan Massa (Hukum Lavoisier)")
            st.info("Antoine Lavoisier (1789) menemukan bahwa dalam sistem tertutup, **massa total zat sebelum reaksi akan selalu sama dengan massa total zat setelah reaksi.**")
            st.latex(r"\text{S}_{(s)} + \text{Fe}_{(s)} \rightarrow \text{FeS}_{(s)}")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write(r"Sebanyak 10 gram besi ($\text{Fe}$) direaksikan dengan 6,4 gram belerang ($\text{S}$) menghasilkan senyawa besi(II) sulfida ($\text{FeS}$) sepenuhnya. Berapakah massa $\text{FeS}$ yang terbentuk?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write(r"Berdasarkan Hukum Kekekalan Massa: Massa $\text{Fe}$ + Massa $\text{S}$ = Massa $\text{FeS}$")
                st.write(r"10 gram + 6,4 gram = **16,4 gram**.")
                
            st.markdown("##### ✍️ Soal Latihan Mandiri")
            st.write(r"Logam magnesium bermassa 4 gram dibakar habis di dalam wadah tertutup. Jika $\text{MgO}$ yang dihasilkan bermassa 6,6 gram, berapakah massa gas oksigen yang ikut bereaksi?")
            st.write("---")

            # --- 2. PROUST ---
            st.subheader("2. Hukum Perbandingan Tetap (Hukum Proust)")
            st.info("Joseph Proust (1799) menyatakan bahwa **perbandingan massa unsur-unsur dalam suatu senyawa adalah selalu tetap dan tertentu.**")
            st.write(r"Contoh senyawa air ($\text{H}_2\text{O}$), perbandingan massa Hidrogen ($\text{H}$) terhadap Oksigen ($\text{O}$) selalu **1 : 8**.")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write(r"Perbandingan massa tembaga ($\text{Cu}$) dan belerang ($\text{S}$) dalam senyawa $\text{CuS}$ adalah 2 : 1. Jika direaksikan 10 gram tembaga dengan 3 gram belerang, berapakah massa $\text{CuS}$ yang terbentuk?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write(r"- $\text{Cu} : \text{S} = 2 : 1$.")
                st.write(r"- $\text{S}$ yang tersedia hanya 3g. Maka $\text{Cu}$ yang bereaksi = $2 \times 3 = 6\text{ gram}$.")
                st.write(r"- Massa $\text{CuS} = 6\text{g (Cu)} + 3\text{g (S)} = $ **9 gram**. (Tersisa 4g $\text{Cu}$).")

            st.markdown("##### ✍️ Soal Latihan Mandiri")
            st.write(r"Perbandingan massa $\text{C}$ dan $\text{O}$ dalam $\text{CO}_2$ adalah 3 : 8. Jika tersedia 12 gram $\text{C}$ dan 40 gram $\text{O}$, tentukan massa $\text{CO}_2$ maksimum!")
            st.write("---")

            # --- 3. DALTON ---
            st.subheader("3. Hukum Perbandingan Berganda (Hukum Dalton)")
            st.info("John Dalton (1803): Jika dua unsur membentuk lebih dari satu senyawa, dan **massa salah satu unsur dibuat sama**, maka **perbandingan massa unsur lainnya berbanding sebagai bilangan bulat dan sederhana.**")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Senyawa I mengandung 40% unsur X, dan Senyawa II mengandung 50% unsur X. Buktikan fenomena ini memenuhi Hukum Dalton!")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("- Senyawa I: X = 40%, Y = 60%. (X : Y = 1 : 1,5)")
                st.write("- Senyawa II: X = 50%, Y = 50%. (X : Y = 1 : 1)")
                st.write("Jika X disamakan (1), perbandingan Y di Senyawa I : II adalah 1,5 : 1 = **3 : 2** (Terbukti bulat dan sederhana).")
            st.write("---")

 
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
        
