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

            # --- 4. GAY-LUSSAC ---
            st.subheader("4. Hukum Perbandingan Volume (Hukum Gay-Lussac)")
            st.info("Joseph Gay-Lussac (1808): Pada suhu dan tekanan yang sama, **volume gas-gas yang bereaksi dan hasil reaksi berbanding sebagai bilangan bulat dan sederhana (sesuai koefisien).**")
            st.latex(r"\text{N}_{2(g)} + 3\text{H}_{2(g)} \rightarrow 2\text{NH}_{3(g)}")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write(r"Gas hidrogen sebanyak 6 Liter direaksikan membentuk uap air: $2\text{H}_{2(g)} + \text{O}_{2(g)} \rightarrow 2\text{H}_2\text{O}_{(g)}$. Berapakah volume uap air yang dihasilkan?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write(r"Koefisien $\text{H}_2 : \text{H}_2\text{O} = 2 : 2 = 1 : 1$. Maka Volume $\text{H}_2\text{O} = $ **6 Liter**.")
            st.write("---")

            # --- 5. AVOGADRO ---
            st.subheader("5. Hipotesis Avogadro")
            st.info("Amadeo Avogadro (1811): Pada suhu dan tekanan yang sama, **semua gas yang volumenya sama akan mengandung jumlah molekul yang sama (Perbandingan Volume = Perbandingan Molekul = Perbandingan Koefisien).**")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write(r"1 Liter gas $\text{N}_2$ mengandung $3 \times 10^{22}$ molekul. Berapa molekul dalam 3 Liter gas $\text{O}_2$ pada kondisi yang sama?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write(r"Volume berbanding lurus dengan molekul. 3 Liter = $3 \times (3 \times 10^{22}) = $ **$9 \times 10^{22}$ molekul**.")


        # ======================================================================
        # TAB 2: KUIS 10 SOAL DENGAN PEMBAHASAN OTOMATIS & VISUAL FEEDBACK
        # ======================================================================
        with tab_kuis:
            st.subheader("✍️ Kuis Evaluasi Level 1 (10 Soal)")
            st.write("Syarat lulus: Minimal benar 8 soal (Skor 80).")
            st.write("---")
            
            q1 = st.radio("1. [Lavoisier] Jika 12 gram Karbon direaksikan dengan 32 gram Oksigen dalam ruang tertutup, massa Karbon Dioksida yang dihasilkan adalah...", ["20 gram", "32 gram", "44 gram", "50 gram"], key="q1")
            q2 = st.radio("2. [Lavoisier] Pemanasan batu kapur menghasilkan 56 gram kapur tohor dan 44 gram gas karbon dioksida. Massa batu kapur sebelum dipanaskan adalah...", ["100 gram", "56 gram", "44 gram", "12 gram"], key="q2")
            q3 = st.radio("3. [Proust] Perbandingan massa H : O dalam air adalah 1 : 8. Jika 4 gram Hidrogen bereaksi dengan 32 gram Oksigen, air yang dihasilkan adalah...", ["36 gram", "40 gram", "32 gram", "8 gram"], key="q3")
            q4 = st.radio("4. [Proust] Perbandingan massa C : O dalam CO2 adalah 3 : 8. Jika 6 gram Karbon direaksikan dengan 20 gram Oksigen, zat yang tersisa adalah...", ["2 gram Karbon", "2 gram Oksigen", "4 gram Karbon", "4 gram Oksigen"], key="q4")
            q5 = st.radio("5. [Dalton] Unsur P dan Q membentuk senyawa I (P=40%) dan senyawa II (P=50%). Jika massa P disamakan, perbandingan massa Q pada senyawa I dan II adalah...", ["1 : 2", "2 : 3", "3 : 2", "4 : 5"], key="q5")
            q6 = st.radio("6. [Dalton] Hukum Kelipatan Berganda (Perbandingan Berganda) dicetuskan oleh...", ["Lavoisier", "Proust", "Dalton", "Avogadro"], key="q6")
            q7 = st.radio("7. [Gay-Lussac] Pada reaksi N2 + 3H2 -> 2NH3, jika butuh 9 Liter H2, volume NH3 yang dihasilkan adalah...", ["3 Liter", "6 Liter", "9 Liter", "12 Liter"], key="q7")
            q8 = st.radio("8. [Gay-Lussac] Volume gas-gas yang bereaksi dan volume gas hasil reaksi berbanding sebagai bilangan bulat dan sederhana, merupakan bunyi hukum...", ["Kekekalan Massa", "Perbandingan Tetap", "Perbandingan Volume", "Hipotesis Avogadro"], key="q8")
            q9 = st.radio("9. [Avogadro] Jika 2 Liter gas CH4 mengandung 10^20 molekul, maka 4 Liter gas CO2 pada P dan T yang sama mengandung molekul sebanyak...", ["10^20", "2 x 10^20", "4 x 10^20", "0.5 x 10^20"], key="q9")
            q10 = st.radio("10. [Avogadro] Menurut Avogadro, perbandingan koefisien reaksi gas sebanding dengan...", ["Massa gas", "Jenis atom", "Suhu gas", "Jumlah molekul dan Volume gas"], key="q10")
            
            st.write("---")
            if st.button("Kirim Lembar Jawaban Kuis 📝"):
                skor = 0
                if q1 == "44 gram": skor += 10
                if q2 == "100 gram": skor += 10
                if q3 == "36 gram": skor += 10
                if q4 == "4 gram Oksigen": skor += 10
                if q5 == "3 : 2": skor += 10
                if q6 == "Dalton": skor += 10
                if q7 == "6 Liter": skor += 10
                if q8 == "Perbandingan Volume": skor += 10
                if q9 == "2 x 10^20": skor += 10
                if q10 == "Jumlah molekul dan Volume gas": skor += 10
                
                if skor >= 80:
                    st.session_state.level_2_terbuka = True
                    st.success(f"🎉 LULUS! KKM Tercapai. Skor kamu: {skor}/100. Kunci Level 2 resmi DIBUKA!")
                    st.balloons()
                else:
                    st.error(f"❌ BELUM LULUS! Skor kamu: {skor}/100 (KKM: 80). Silakan pelajari pembahasan di bawah dan coba lagi!")
                
                st.markdown("### 💡 Kunci Jawaban & Pembahasan")
                st.info("1. **44 gram** (Lavoisier: 12g + 32g = 44g)\n"
                        "2. **100 gram** (Lavoisier: 56g + 44g = 100g)\n"
                        "3. **36 gram** (Proust: Semua habis bereaksi karena 4:32 sama dengan 1:8, hasil = 4+32=36g)\n"
                        "4. **4 gram Oksigen** (Proust: C=6g butuh O=16g. Tersedia 20g Oksigen, sisa 20-16 = 4g Oksigen)\n"
                        "5. **3 : 2** (Dalton: Senyawa I Q=60/40=1.5. Senyawa II Q=50/50=1. Perbandingan 1.5 : 1 = 3 : 2)\n"
                        "6. **Dalton** (Teori Kelipatan Berganda adalah milik John Dalton)\n"
                        "7. **6 Liter** (Gay-Lussac: Koef NH3/H2 x Vol H2 = 2/3 x 9L = 6L)\n"
                        "8. **Perbandingan Volume** (Bunyi Hukum Gay-Lussac)\n"
                        "9. **2 x 10^20** (Avogadro: Volume 2x lipat (4L vs 2L), maka molekul juga 2x lipat)\n"
                        "10. **Jumlah molekul dan Volume gas** (Inti hipotesis Avogadro)")
                
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
        
