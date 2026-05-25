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
elif st.session_state.get('menu_aktif') == 'dashboard' or st.session_state.get('menu_aktif') is None:
    if st.session_state.get('menu_aktif') is None:
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()

    st.success(f"{teks[lang]['berhasil']} {st.session_state.username}! 🎉")
    
    st.title("📋 Dashboard Utama")
    st.write("Silakan pilih level pembelajaran di bawah ini:")
    
    # Inisialisasi status kunci level jika belum ada di memori
    if 'level_2_terbuka' not in st.session_state:
        st.session_state.level_2_terbuka = False
    if 'level_3_terbuka' not in st.session_state:
        st.session_state.level_3_terbuka = False

        # --- TOMBOL LEVEL 1 (Selalu Terbuka) ---
    if st.button("🚀 Masuk ke Level 1: Hukum Dasar Kimia"):
        st.session_state.menu_aktif = 'level_1'
        st.rerun()

    # --- TOMBOL LEVEL 2 (Bebas Akses / Tanpa Kunci) ---
    st.write("---")
    if st.button("🎮 Masuk ke Level 2: Konsep Mol & Stoikiometri"):
        st.session_state.menu_aktif = 'level_2'
        st.rerun()

    # --- TOMBOL LEVEL 3 (Bebas Akses / Tanpa Kunci) ---
    st.write("---")
    if st.button("🔥 Masuk ke Level 3: Perhitungan Persamaan Reaksi"):
        st.session_state.menu_aktif = 'level_3'
        st.rerun()
        
elif st.session_state.get('menu_aktif') == 'level_1':
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 1: Hukum Dasar Kimia")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 1"])

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
            st.write("Berdasarkan Hukum Kekekalan Massa:")
            st.latex(r"\text{Massa Sebelum Reaksi} = \text{Massa Sesudah Reaksi}")
            st.latex(r"\text{Massa Fe} + \text{Massa S} = \text{Massa FeS}")
            st.latex(r"10\text{ gram} + 6,4\text{ gram} = 16,4\text{ gram}")
            
        st.markdown("##### ✍️ Soal Latihan Mandiri (Tanpa Pembahasan)")
        st.write(r"Logam magnesium bermassa 4 gram dibakar habis di dalam wadah tertutup dengan gas oksigen. Jika senyawa magnesium oksida ($\text{MgO}$) yang dihasilkan bermassa 6,6 gram, berapakah massa gas oksigen yang ikut bereaksi?")
        st.text_input("Tulis jawabanmu di sini (contoh: 2,6 gram):", key="tanya_lavoisier")
        st.write("---")

        # --- 2. PROUST ---
        st.subheader("2. Hukum Perbandingan Tetap (Hukum Proust)")
        st.info("Joseph Proust (1799) menyatakan bahwa **perbandingan massa unsur-unsur dalam suatu senyawa adalah selalu tetap dan tertentu.**")
        st.write(r"Contoh senyawa air ($\text{H}_2\text{O}$), perbandingan massa Hidrogen ($\text{H}$) terhadap Oksigen ($\text{O}$) selalu **1 : 8**.")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Perbandingan massa tembaga ($\text{Cu}$) dan belerang ($\text{S}$) dalam senyawa $\text{CuS}$ adalah 2 : 1. Jika direaksikan 10 gram tembaga dengan 3 gram belerang, berapakah massa $\text{CuS}$ yang terbentuk?")
        with st.expander("Klik di sini untuk melihat Pembahasan"):
            st.write("Mari kita hitung menggunakan pecahan per perbandingan:")
            st.latex(r"\text{Perbandingan massa Cu} : \text{S} = 2 : 1")
            st.write("Jika semua belerang (3 gram) habis bereaksi, massa tembaga yang dibutuhkan adalah:")
            st.latex(r"\text{Massa Cu yang bereaksi} = \frac{2}{1} \times 3\text{ gram} = 6\text{ gram}")
            st.write("Karena tersedia 10 gram tembaga, maka tembaga berlebih (tersisa sebanyak 4 gram).")
            st.write("Massa senyawa yang terbentuk:")
            st.latex(r"\text{Massa CuS} = 6\text{ gram (Cu)} + 3\text{ gram (S)} = 9\text{ gram}")

        st.markdown("##### ✍️ Soal Latihan Mandiri (Tanpa Pembahasan)")
        st.write(r"Perbandingan massa unsur $\text{C}$ dan unsur $\text{O}$ dalam senyawa karbon dioksida ($\text{CO}_2$) adalah 3 : 8. Jika tersedia 12 gram Karbon dan 40 gram Oksigen, tentukan massa $\text{CO}_2$ maksimum yang dapat terbentuk!")
        st.text_input("Tulis jawabanmu di sini (contoh: 44 gram):", key="tanya_proust")
        st.write("---")

        # --- 3. DALTON ---
        st.subheader("3. Hukum Perbandingan Berganda (Hukum Dalton)")
        st.info("John Dalton (1803): Jika dua unsur membentuk lebih dari satu senyawa, dan **massa salah satu unsur dibuat sama**, maka **perbandingan massa unsur lainnya berbanding sebagai bilangan bulat dan sederhana.**")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write("Unsur X dan Y membentuk dua jenis senyawa. Senyawa I mengandung 40% unsur X, dan Senyawa II mengandung 50% unsur X. Buktikan fenomena ini memenuhi Hukum Dalton!")
        with st.expander("Klik di sini untuk melihat Pembahasan"):
            st.write("Senyawa I: Unsur X = 40%, maka unsur Y = 60%.")
            st.latex(r"\text{Rasio Senyawa I } \left(\frac{\text{Massa Y}}{\text{Massa X}}\right) = \frac{60\%}{40\%} = 1,5")
            st.write("Senyawa II: Unsur X = 50%, maka unsur Y = 50%.")
            st.latex(r"\text{Rasio Senyawa II } \left(\frac{\text{Massa Y}}{\text{Massa X}}\right) = \frac{50\%}{50\%} = 1")
            st.write("Jika massa X dibuat sama-sama bernilai 1, perbandingan massa unsur Y pada Senyawa I dan Senyawa II menjadi:")
            st.latex(r"\text{Perbandingan Y}_I : \text{Y}_{II} = 1,5 : 1 = 3 : 2")
            st.write("Perbandingan **3 : 2** adalah bilangan bulat dan sederhana, terbukti memenuhi Hukum Dalton!")
            
        st.markdown("##### ✍️ Soal Latihan Mandiri (Tanpa Pembahasan)")
        st.write("Dua buah senyawa belerang oksida dianalisis. Senyawa A mengandung 50% belerang, sedangkan senyawa B mengandung 40% belerang. Jika massa belerang disamakan, berapakah perbandingan massa Oksigen pada senyawa A terhadap senyawa B?")
        st.text_input("Tulis jawabanmu di sini (contoh: 2 : 3):", key="tanya_dalton")
        st.write("---")

        # --- 4. GAY-LUSSAC ---
        st.subheader("4. Hukum Perbandingan Volume (Hukum Gay-Lussac)")
        st.info("Joseph Gay-Lussac (1808): Pada suhu dan tekanan yang sama, **volume gas-gas yang bereaksi dan hasil reaksi berbanding sebagai bilangan bulat dan sederhana (sesuai koefisien reaksinya).**")
        st.latex(r"\text{N}_{2(g)} + 3\text{H}_{2(g)} \rightarrow 2\text{NH}_{3(g)}")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Gas hidrogen sebanyak 6 Liter direaksikan dengan gas oksigen membentuk uap air: $2\text{H}_{2(g)} + \text{O}_{2(g)} \rightarrow 2\text{H}_2\text{O}_{(g)}$. Berapakah volume uap air yang dihasilkan?")
        with st.expander("Klik di sini untuk melihat Pembahasan"):
            st.write("Gunakan rumus perbandingan koefisien bertingkat:")
            st.latex(r"\text{Volume H}_2\text{O} = \frac{\text{Koefisien H}_2\text{O}}{\text{Koefisien H}_2} \times \text{Volume H}_2")
            st.latex(r"\text{Volume H}_2\text{O} = \frac{2}{2} \times 6\text{ Liter} = 6\text{ Liter}")
            
        st.markdown("##### ✍️ Soal Latihan Mandiri (Tanpa Pembahasan)")
        st.write(r"Pada suhu dan tekanan yang sama, gas metana ($\text{CH}_4$) dibakar dengan gas oksigen menurut persamaan: $\text{CH}_{4(g)} + 2\text{O}_{2(g)} \rightarrow \text{CO}_{2(g)} + 2\text{H}_2\text{O}_{(g)}$. Jika digunakan 3 Liter gas metana, berapakah volume gas oksigen yang dibutuhkan?")
        st.text_input("Tulis jawabanmu di sini (contoh: 6 Liter):", key="tanya_gay")
        st.write("---")

        # --- 5. AVOGADRO ---
        st.subheader("5. Hipotesis Avogadro")
        st.info("Amadeo Avogadro (1811): Pada suhu dan tekanan yang sama, **semua gas yang volumenya sama akan mengandung jumlah molekul yang sama.**")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Pada suhu dan tekanan tertentu, 1 Liter gas $\text{N}_2$ mengandung $3 \times 10^{22}$ molekul. Berapa jumlah molekul dalam 3 Liter gas $\text{O}_2$ pada kondisi yang sama?")
        with st.expander("Klik di sini untuk melihat Pembahasan"):
            st.write("Perbandingan jumlah molekul berbanding lurus dengan perbandingan volumenya:")
            st.latex(r"\text{Jumlah Molekul O}_2 = \frac{\text{Volume O}_2}{\text{Volume N}_2} \times \text{Jumlah Molekul N}_2")
            st.latex(r"\text{Jumlah Molekul O}_2 = \frac{3\text{ Liter}}{1\text{ Liter}} \times (3 \times 10^{22}) = 9 \times 10^{22}\text{ molekul}")

        st.markdown("##### ✍️ Soal Latihan Mandiri (Tanpa Pembahasan)")
        st.write(r"Jika 5 Liter gas hidrogen ($\text{H}_2$) mengandung sebanyak $2 \times 10^{23}$ molekul, berapakah jumlah molekul yang terdapat dalam 15 Liter gas karbon monoksida ($\text{CO}$) jika diukur pada suhu dan tekanan yang sama?")
        st.text_input("Tulis jawabanmu di sini:", key="tanya_avogadro")


    with tab_kuis:
        st.subheader("✍️ Kuis Evaluasi Level 1 (10 Soal)")
        st.write("Syarat lulus: Minimal benar 8 soal (Skor 80).")
        st.write("---")
        
        q1 = st.radio("1.Jika 12 gram Karbon direaksikan dengan 32 gram Oksigen dalam ruang tertutup, massa Karbon Dioksida yang dihasilkan adalah...", ["20 gram", "32 gram", "44 gram", "50 gram"], key="q1")
        q2 = st.radio("2.Pemanasan batu kapur menghasilkan 56 gram kapur tohor dan 44 gram gas karbon dioksida. Massa batu kapur sebelum dipanaskan adalah...", ["100 gram", "56 gram", "44 gram", "12 gram"], key="q2")
        q3 = st.radio("3.Perbandingan massa H : O dalam air adalah 1 : 8. Jika 4 gram Hidrogen bereaksi dengan 32 gram Oksigen, air yang dihasilkan adalah...", ["36 gram", "40 gram", "32 gram", "8 gram"], key="q3")
        q4 = st.radio("4.Perbandingan massa C : O dalam CO2 adalah 3 : 8. Jika 6 gram Karbon direaksikan dengan 20 gram Oksigen, zat yang tersisa adalah...", ["2 gram Karbon", "2 gram Oksigen", "4 gram Karbon", "4 gram Oksigen"], key="q4")
        q5 = st.radio("5.Unsur P dan Q membentuk senyawa I (P=40%) dan senyawa II (P=50%). Jika massa P disamakan, perbandingan massa Q pada senyawa I dan II adalah...", ["1 : 2", "2 : 3", "3 : 2", "4 : 5"], key="q5")
        q6 = st.radio("6.Hukum Kelipatan Berganda (Perbandingan Berganda) dicetuskan oleh...", ["Lavoisier", "Proust", "Dalton", "Avogadro"], key="q6")
        q7 = st.radio("7.Pada reaksi N2 + 3H2 -> 2NH3, jika butuh 9 Liter H2, volume NH3 yang dihasilkan adalah...", ["3 Liter", "6 Liter", "9 Liter", "12 Liter"], key="q7")
        q8 = st.radio("8.Volume gas-gas yang bereaksi dan volume gas hasil reaksi berbanding sebagai bilangan bulat dan sederhana, merupakan bunyi hukum...", ["Kekekalan Massa", "Perbandingan Tetap", "Perbandingan Volume", "Hipotesis Avogadro"], key="q8")
        q9 = st.radio("9.Jika 2 Liter gas CH4 mengandung 10^20 molekul, maka 4 Liter gas CO2 pada P dan T yang sama mengandung molekul sebanyak...", ["10^20", "2 x 10^20", "4 x 10^20", "0.5 x 10^20"], key="q9")
        q10 = st.radio("10.Menurut Avogadro, perbandingan koefisien reaksi gas sebanding dengan...", ["Massa gas", "Jenis atom", "Suhu gas", "Jumlah molekul dan Volume gas"], key="q10")
        st.write("---")
        if st.button("Periksa Hasil Jawaban & Lihat Pembahasan Level 1 📝"):
            skor_hitung = 0
            if q1 == "36 gram": skor_hitung += 1
            if q2 == "22 gram": skor_hitung += 1
            if q3 == "1 : 8": skor_hitung += 1
            if q4 == "3 : 8": skor_hitung += 1
            if q5 == "Senyawa I": skor_hitung += 1
            if q6 == "John Dalton": skor_hitung += 1
            if q7 == "6 Liter": skor_hitung += 1
            if q8 == "Gay-Lussac": skor_hitung += 1
            if q9 == "2 x 10^20 molekul": skor_hitung += 1
            if q10 == "Perbandingan Volume": skor_hitung += 1
            
            skor_final = round((skor_hitung / 10) * 100)
            st.success(f"Evaluasi selesai! Kamu menjawab {skor_hitung} dari 10 soal dengan benar. Skor kamu: {skor_final} / 100.")
            if skor_final >= 80:
                st.balloons()
                st.success("Selamat! Kamu lulus Level 1 dan siap melaju ke Level 2!")
            else:
                st.warning("Skor kamu di bawah 80. Yuk pelajari lagi pembahasannya di bawah ini agar lebih paham!")
                
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Detil Level 1:")
            
            st.markdown("**Soal 1 (Hukum Kekekalan Massa / Lavoisier)**")
            st.write("Massa zat sebelum reaksi sama dengan massa zat setelah reaksi.")
            st.latex(r"\text{Massa produk} = 12 \text{ gram Karbon} + 32 \text{ gram Oksigen} = 44 \text{ gram}")
            
            st.markdown("**Soal 2 (Hukum Lavoisier)**")
            st.latex(r"\text{Massa Gas CO}_2 = \text{Massa Batu Kapur} - \text{Massa Kapur Tohor} = 56 \text{ gram} - 34 \text{ gram} = 22 \text{ gram}")
            
            st.markdown("**Soal 3 (Hukum Perbandingan Tetap / Proust)**")
            st.write("Perbandingan massa H : O selalu tetap yaitu 1 : 8.")
            
            st.markdown("**Soal 4 (Hukum Proust)**")
            st.write("Massa C : O = 3 : 8. Jika Karbon 6 gram (2 kali lipat), maka Oksigen yang dibutuhkan juga 2 kali lipat (16 gram).")
            
            st.markdown("**Soal 5 (Hukum Perbandingan Berganda / Dalton)**")
            st.write("Jika massa salah satu unsur dibuat tetap, maka perbandingan massa unsur lainnya dalam senyawa-senyawa tersebut akan merupakan bilangan bulat dan sederhana.")
            
            st.markdown("**Soal 6 (Sejarah Hukum Kimia)**")
            st.write("Hukum Kelipatan Berganda dicetuskan oleh **John Dalton** pada tahun 1803.")
            
            st.markdown("**Soal 7 (Hukum Perbandingan Volume / Gay-Lussac)**")
            st.write("Perbandingan volume gas sesuai dengan perbandingan koefisien reaksinya:")
            st.latex(r"\text{Volume NH}_3 = \frac{\text{Koefisien NH}_3}{\text{Koefisien H}_2} \times \text{Volume H}_2 = \frac{2}{3} \times 9 \text{ Liter} = 6 \text{ Liter}")
            
            st.markdown("**Soal 8 (Pencetus Hukum Gas)**")
            st.write("Hukum yang menyatakan volume gas sebanding dengan koefisien reaksi dicetuskan oleh **Gay-Lussac**.")
            
            st.markdown("**Soal 9 (Hukum Avogadro)**")
            st.write("Pada suhu dan tekanan yang sama, gas-gas yang volumenya sama mengandung jumlah molekul yang sama pula.")
            st.latex(r"\text{Jumlah Molekul CO}_2 = \frac{4 \text{ Liter}}{2 \text{ Liter}} \times 10^{20} = 2 \times 10^{20} \text{ molekul}")
            
            st.markdown("**Soal 10 (Inti Hukum Avogadro)**")
            st.write("Menurut Avogadro, perbandingan koefisien reaksi gas sebanding dengan **perbandingan volume** gas-gas tersebut.")
            
# ==================================================
# TOMBOL LOGOUT (Selalu di paling bawah)
# ==================================================
st.write("---")
if st.button("Keluar / Logout"):
    st.session_state.sudah_login = False
    st.session_state.username = ""
    if 'menu_aktif' in st.session_state:
        del st.session_state.menu_aktif
    st.rerun()
    
