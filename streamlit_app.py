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

    # --- TOMBOL LEVEL 2 (Terkunci sampai Level 1 Lulus) ---
    st.write("---")
    if st.session_state.level_2_terbuka:
        if st.button("🔓 Masuk ke Level 2: Konsep Mol & Stoikiometri"):
            st.session_state.menu_aktif = 'level_2'
            st.rerun()
    else:
        st.button("🔒 Level 2: Konsep Mol & Stoikiometri (Terkunci - Luluskan Kuis Level 1)", disabled=True)

    # --- TOMBOL LEVEL 3 (Terkunci sampai Level 2 Lulus) ---
    if st.session_state.level_3_terbuka:
        if st.button("🔓 Masuk ke Level 3: Perhitungan Persamaan Reaksi"):
            st.session_state.menu_aktif = 'level_3'
            st.rerun()
    else:
        st.button("🔒 Level 3: Perhitungan Persamaan Reaksi (Terkunci - Luluskan Kuis Level 2)", disabled=True)


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
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Lengkap (Pecahan Vertikal)")
            
            st.markdown("**1. [Hukum Lavoisier] Jawaban: 44 gram**")
            st.latex(r"\text{Massa Karbon} + \text{Massa Oksigen} = \text{Massa CO}_2 \implies 12\text{ g} + 32\text{ g} = 44\text{ gram}")
            
            st.markdown("**2. [Hukum Lavoisier] Jawaban: 100 gram**")
            st.latex(r"\text{Massa Kapur Tumpuk} = 56\text{ g Kapur Tohor} + 44\text{ g CO}_2 = 100\text{ gram}")
            
            st.markdown("**3. [Hukum Proust] Jawaban: 36 gram**")
            st.latex(r"\text{Perbandingan H} : \text{O} = 1 : 8. \text{ Massa total air } = 4\text{ g Hidrogen} + 32\text{ g Oksigen} = 36\text{ gram}")
            
            st.markdown("**4. [Hukum Proust] Jawaban: 4 gram Oksigen**")
            st.latex(r"\text{Massa Oksigen bereaksi} = \frac{8}{3} \times 6\text{ g Karbon} = 16\text{ gram}")
            st.latex(r"\text{Sisa Oksigen} = 20\text{ g (tersedia)} - 16\text{ g (bereaksi)} = 4\text{ gram}")
            
            st.markdown("**5. [Hukum Dalton] Jawaban: 3 : 2**")
            st.latex(r"\text{Senyawa I: } \frac{\text{Massa Q}}{\text{Massa P}} = \frac{60\%}{40\%} = 1,5 \quad \text{dan Senyawa II: } \frac{\text{Massa Q}}{\text{Massa P}} = \frac{50\%}{50\%} = 1")
            st.latex(r"\text{Perbandingan massa Q} = 1,5 : 1 = 3 : 2")
            
            st.markdown("**6. [Hukum Dalton] Jawaban: Dalton** (Teori Kelipatan Berganda dicanangkan oleh John Dalton)")
            
            st.markdown("**7. [Hukum Gay-Lussac] Jawaban: 6 Liter**")
            st.latex(r"\text{Volume NH}_3 = \frac{\text{Koefisien NH}_3}{\text{Koefisien H}_2} \times \text{Volume H}_2 = \frac{2}{3} \times 9\text{ L} = 6\text{ Liter}")
            
            st.markdown("**8. [Hukum Gay-Lussac] Jawaban: Perbandingan Volume** (Bunyi Hukum Gay-Lussac)")
            
            st.markdown("**9. [Hipotesis Avogadro] Jawaban: 2 x 10^20**")
            st.latex(r"\text{Jumlah molekul CO}_2 = \frac{\text{Volume CO}_2}{\text{Volume CH}_4} \times \text{Molekul CH}_4 = \frac{4\text{ L}}{2\text{ L}} \times 10^{20} = 2 \times 10^{20}")
            
            st.markdown("**10. [Hipotesis Avogadro] Jawaban: Jumlah molekul dan Volume gas** (Inti dari hipotesis Amadeo Avogadro)")

elif st.session_state.get('menu_aktif') == 'level_2':
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 2: Konsep Mol & Stoikiometri")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 2"])

    with tab_materi:
        st.write("Pelajari konsep mol di bawah ini, ini adalah jantungnya perhitungan kimia!")
        st.write("---")

        # --- 1. Mol dan Massa ---
        st.subheader("1. Hubungan Mol dengan Massa (Gram)")
        st.info("Satu mol zat apa pun memiliki massa yang angkanya sama persis dengan Ar (Massa Atom Relatif) atau Mr (Massa Molekul Relatif) zat tersebut.")
        st.latex(r"\text{Jumlah Mol } (n) = \frac{\text{Massa (gram)}}{\text{Ar atau Mr}}")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa jumlah mol dari 18 gram air ($\text{H}_2\text{O}$)? (Diketahui: Ar H = 1, O = 16)")

elif st.session_state.get('menu_aktif') == 'level_2':
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 2: Konsep Mol & Stoikiometri Senyawa")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 2"])

    with tab_materi:
        st.markdown("### 🌉 Jembatan Mol: Pusat Perhitungan Kimia")
        st.write("Dalam kimia, **Mol ($n$)** adalah terminal pusat. Semua konversi (massa, volume, partikel, konsentrasi) harus melewati 'Jembatan Mol'. Hafalkan peta konsep dasar ini:")
        st.info("1. **Massa (gram)** $\leftrightarrow$ Mol $\leftrightarrow$ **Volume Gas (L)**\n"
                "2. **Jumlah Partikel** $\leftrightarrow$ Mol $\leftrightarrow$ **Molaritas (M)**")
        st.write("---")

        # --- 1. Mol dan Massa ---
        st.subheader("1. Hubungan Mol dengan Massa")
        st.latex(r"n = \frac{\text{Massa (gram)}}{\text{Ar atau Mr}} \quad \text{atau} \quad \text{Massa} = n \times \text{Mr}")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Hitunglah jumlah mol dari 31,5 gram $\text{HNO}_3$! (Ar H=1, N=14, O=16)")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"\text{Mr HNO}_3 = 1 + 14 + (3 \times 16) = 63")
            st.latex(r"n = \frac{31,5\text{ gram}}{63} = 0,5\text{ mol}")
            
        st.markdown("##### ✍️ Latihan Mandiri")
        st.write(r"Berapa massa dari 0,2 mol kalsium karbonat ($\text{CaCO}_3$)? (Ar Ca=40, C=12, O=16)")
        st.text_input("Tulis jawabanmu (contoh: 20 gram):", key="l2_m1")
        st.write("---")

        # --- 2. Mol dan Jumlah Partikel ---
        st.subheader("2. Hubungan Mol dengan Jumlah Partikel")
        st.write("Satu mol zat mengandung partikel sebanyak Bilangan Avogadro ($L = 6,02 \times 10^{23}$).")
        st.latex(r"n = \frac{\text{Jumlah Partikel}}{6,02 \times 10^{23}} \quad \text{atau} \quad \text{Jumlah Partikel} = n \times (6,02 \times 10^{23})")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa jumlah atom Besi ($\text{Fe}$) dalam 0,1 mol paku besi?")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"\text{Jumlah atom} = 0,1 \times (6,02 \times 10^{23}) = 6,02 \times 10^{22} \text{ atom}")

        st.markdown("##### ✍️ Latihan Mandiri")
        st.write(r"Suatu sampel mengandung $3,01 \times 10^{23}$ molekul air. Berapa mol air tersebut?")
        st.text_input("Tulis jawabanmu (contoh: 0,5 mol):", key="l2_m2")
        st.write("---")

        # --- 3. Mol dan Volume Gas ---
        st.subheader("3. Hubungan Mol dengan Volume Gas")
        st.write("Volume gas sangat bergantung pada suhu (T) dan tekanan (P). Ada 3 kondisi utama:")
        st.markdown("**A. Keadaan Standar / STP (0°C, 1 atm)**")
        st.latex(r"\text{Volume}_{STP} = n \times 22,4\text{ L/mol}")
        st.markdown("**B. Keadaan Ruang / RTP (25°C, 1 atm)**")
        st.latex(r"\text{Volume}_{RTP} = n \times 24\text{ L/mol}")
        st.markdown("**C. Gas Ideal (Suhu & Tekanan Tertentu)**")
        st.latex(r"P \times V = n \times R \times T")
        st.caption("P = Tekanan (atm), V = Volume (L), R = 0,082 L.atm/mol.K, T = Suhu (Kelvin = °C + 273)")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa volume 8 gram gas $\text{CH}_4$ (Mr=16) pada suhu 27°C dan tekanan 1 atm? (R=0,082)")
        with st.expander("Lihat Pembahasan"):
            st.write("Langkah 1: Ubah massa ke mol (Jembatan Mol).")
            st.latex(r"n = \frac{8\text{ g}}{16} = 0,5\text{ mol}")
            st.write("Langkah 2: Gunakan rumus Gas Ideal ($T = 27 + 273 = 300\text{ K}$).")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{0,5 \times 0,082 \times 300}{1} = 12,3\text{ Liter}")

        st.markdown("##### ✍️ Latihan Mandiri")
        st.write("Berapa volume dari 0,2 mol gas oksigen pada keadaan STP?")
        st.text_input("Tulis jawabanmu (contoh: 4,48 Liter):", key="l2_m3")
        st.write("---")

        # --- 4. Mol dan Molaritas ---
        st.subheader("4. Hubungan Mol dengan Molaritas (Konsentrasi Larutan)")
        st.write("Molaritas (M) menyatakan jumlah mol zat terlarut dalam tiap 1 Liter larutan.")
        st.latex(r"M = \frac{n}{V\text{ (Liter)}} \quad \text{atau} \quad n = M \times V\text{ (Liter)}")

        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa Molaritas larutan jika 4 gram $\text{NaOH}$ (Mr=40) dilarutkan dalam air hingga volumenya 500 mL?")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"n = \frac{4\text{ g}}{40} = 0,1\text{ mol} \quad \text{dan} \quad V = 500\text{ mL} = 0,5\text{ L}")
            st.latex(r"M = \frac{0,1\text{ mol}}{0,5\text{ L}} = 0,2\text{ Molar}")

        st.write("---")

        # --- 5. Stoikiometri Senyawa ---
        st.subheader("5. Stoikiometri Senyawa (Kadar & Rumus Empiris)")
        st.write("**A. Kadar Unsur dalam Senyawa:**")
        st.latex(r"\% \text{Unsur} = \frac{\text{Jumlah atom} \times \text{Ar}}{\text{Mr Senyawa}} \times 100\%")
        st.write("**B. Rumus Empiris (RE) & Rumus Molekul (RM):**")
        st.info("Rumus Empiris adalah perbandingan mol paling sederhana dari unsur-unsur pembentuk senyawa. \nRumus Molekul adalah $(RE)_n = Mr$.")

    with tab_kuis:
        st.subheader("✍️ Kuis Evaluasi Level 2 (15 Soal Komprehensif)")
        st.write("Syarat lulus: Minimal benar 12 soal (Skor KKM: 80).")
        st.write("---")
        
        st.markdown("**Bagian 1: Konsep Mol Dasar (Massa & Partikel)**")
        q1 = st.radio("1. Jika Ar Fe=56, berapakah massa dari 0,5 mol logam besi?", ["28 gram", "56 gram", "112 gram", "14 gram"], key="l2q1")
        q2 = st.radio("2. Berapakah jumlah mol dari 9,8 gram H2SO4? (Mr = 98)", ["0,01 mol", "0,1 mol", "1 mol", "10 mol"], key="l2q2")
        q3 = st.radio("3. Satu mol suatu senyawa selalu mengandung...", ["Satu gram zat", "22,4 Liter pada suhu berapapun", "6,02 x 10^23 partikel", "Massa yang sama dengan air"], key="l2q3")
        q4 = st.radio("4. Berapa jumlah molekul yang terdapat dalam 0,2 mol gas O2?", ["1,204 x 10^23 molekul", "3,01 x 10^23 molekul", "6,02 x 10^22 molekul", "1,204 x 10^22 molekul"], key="l2q4")
        q5 = st.radio("5. Suatu sampel mengandung 3,01 x 10^23 atom Karbon. Berapakah massa sampel tersebut? (Ar C=12)", ["3 gram", "6 gram", "12 gram", "24 gram"], key="l2q5")

        st.markdown("**Bagian 2: Jembatan Mol (Volume & Molaritas)**")
        q6 = st.radio("6. Berapa volume dari 0,5 mol gas N2 pada keadaan STP (0°C, 1 atm)?", ["11,2 L", "22,4 L", "5,6 L", "44,8 L"], key="l2q6")
        q7 = st.radio("7. Jika volume gas CO2 pada keadaan RTP (25°C, 1 atm) adalah 12 Liter, berapa mol gas tersebut?", ["0,2 mol", "0,5 mol", "1 mol", "2 mol"], key="l2q7")
        q8 = st.radio("8. Massa dari 5,6 Liter gas SO2 pada keadaan STP adalah... (Ar S=32, O=16, Mr=64)", ["8 gram", "16 gram", "32 gram", "64 gram"], key="l2q8")
        q9 = st.radio("9. Jika 2 mol gas O2 berada dalam tabung pada suhu 27°C (300K) dan tekanan 2 atm (R=0,082), volumenya adalah...", ["12,3 L", "24,6 L", "30 L", "49,2 L"], key="l2q9")
        q10 = st.radio("10. Sebanyak 5,85 gram NaCl (Mr=58,5) dilarutkan dalam air hingga volumenya 250 mL. Molaritas larutan tersebut adalah...", ["0,1 M", "0,2 M", "0,4 M", "1,0 M"], key="l2q10")

        st.markdown("**Bagian 3: Stoikiometri Senyawa & Campuran**")
        q11 = st.radio("11. Berapakah persentase massa unsur Karbon (Ar C=12) dalam senyawa CO(NH2)2 (Mr=60)?", ["12%", "20%", "24%", "40%"], key="l2q11")
        q12 = st.radio("12. Suatu senyawa memiliki rumus empiris CH2. Jika Mr senyawa tersebut adalah 42, maka rumus molekulnya adalah... (Ar C=12, H=1)", ["C2H4", "C3H6", "C4H8", "C5H10"], key="l2q12")
        q13 = st.radio("13. Senyawa hidrokarbon mengandung 80% Karbon dan 20% Hidrogen. Rumus empirisnya adalah... (Ar C=12, H=1)", ["CH2", "CH3", "C2H4", "C2H6"], key="l2q13")
        q14 = st.radio("14. Volume larutan HCl 0,2 M yang mengandung 0,1 mol HCl adalah...", ["200 mL", "250 mL", "500 mL", "1000 mL"], key="l2q14")
        q15 = st.radio("15. [Tantangan] Massa 3,01 x 10^23 molekul gas X adalah 22 gram. Berapakah volume gas X tersebut pada keadaan STP?", ["5,6 Liter", "11,2 Liter", "22,4 Liter", "44,8 Liter"], key="l2q15")

        st.write("---")
        if st.button("Kirim Lembar Jawaban Level 2 📝"):
            jawaban_benar = 0
            if q1 == "28 gram": jawaban_benar += 1
            if q2 == "0,1 mol": jawaban_benar += 1
            if q3 == "6,02 x 10^23 partikel": jawaban_benar += 1
            if q4 == "1,204 x 10^23 molekul": jawaban_benar += 1
            if q5 == "6 gram": jawaban_benar += 1
            if q6 == "11,2 L": jawaban_benar += 1
            if q7 == "0,5 mol": jawaban_benar += 1
            if q8 == "16 gram": jawaban_benar += 1
            if q9 == "24,6 L": jawaban_benar += 1
            if q10 == "0,4 M": jawaban_benar += 1
            if q11 == "20%": jawaban_benar += 1
            if q12 == "C3H6": jawaban_benar += 1
            if q13 == "CH3": jawaban_benar += 1
            if q14 == "500 mL": jawaban_benar += 1
            if q15 == "11,2 Liter": jawaban_benar += 1
            
            skor = round((jawaban_benar / 15) * 100)
            
            if skor >= 80:
                st.session_state.level_3_terbuka = True
                st.success(f"🎉 LULUS! Kamu benar {jawaban_benar} dari 15 soal. Skor kamu: {skor}. Kunci Level 3 resmi DIBUKA!")
                st.balloons()
            else:
                st.error(f"❌ BELUM LULUS! Kamu baru benar {jawaban_benar} dari 15 soal. Skor kamu: {skor} (KKM: 80). Silakan baca lagi peta Jembatan Mol di pembahasan!")
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Lengkap")
            
            st.info("1. **28 gram**")
            st.latex(r"\text{Massa} = 0,5\text{ mol} \times 56 = 28\text{ g}")
            
            st.info("2. **0,1 mol**")
            st.latex(r"n = \frac{9,8\text{ g}}{98} = 0,1\text{ mol}")
            
            st.info("3. **6,02 x 10^23 partikel** (Definisi tetapan Avogadro)")
            
            st.info("4. **1,204 x 10^23 molekul**")
            st.latex(r"\text{Molekul} = 0,2 \times (6,02 \times 10^{23}) = 1,204 \times 10^{23}")
            
            st.info("5. **6 gram**")
            st.latex(r"n = \frac{3,01 \times 10^{23}}{6,02 \times 10^{23}} = 0,5\text{ mol}. \quad \text{Massa} = 0,5 \times 12 = 6\text{ g}")
            
            st.info("6. **11,2 L**")
            st.latex(r"V = 0,5\text{ mol} \times 22,4 = 11,2\text{ L}")
            
            st.info("7. **0,5 mol**")
            st.latex(r"n = \frac{12\text{ L}}{24\text{ (RTP)}} = 0,5\text{ mol}")
            
            st.info("8. **16 gram**")
            st.latex(r"n = \frac{5,6}{22,4} = 0,25\text{ mol}. \quad \text{Massa} = 0,25 \times 64 = 16\text{ g}")
            
            st.info("9. **24,6 L** (Gas Ideal)")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{2 \times 0,082 \times 300}{2} = 24,6\text{ L}")
            
            st.info("10. **0,4 M**")
            st.latex(r"n = \frac{5,85}{58,5} = 0,1\text{ mol}. \quad M = \frac{0,1\text{ mol}}{0,25\text{ L}} = 0,4\text{ M}")

            st.info("11. **20%**")
            st.latex(r"\% C = \frac{1 \times 12}{60} \times 100\% = 20\%")
elif st.session_state.get('menu_aktif') == 'level_2':
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 2: Konsep Mol & Stoikiometri Senyawa")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 2"])

    with tab_materi:
        st.markdown("### 🌉 Jembatan Mol: Pusat Perhitungan Kimia")
        st.write("Dalam kimia, **Mol ($n$)** adalah terminal pusat. Semua konversi (massa, volume, partikel, konsentrasi) harus melewati 'Jembatan Mol'. Hafalkan peta konsep dasar ini:")
        st.info("1. **Massa (gram)** $\leftrightarrow$ Mol $\leftrightarrow$ **Volume Gas (L)**\n"
                "2. **Jumlah Partikel** $\leftrightarrow$ Mol $\leftrightarrow$ **Molaritas (M)**")
        st.write("---")

        # --- 1. Mol dan Massa ---
        st.subheader("1. Hubungan Mol dengan Massa")
        st.latex(r"n = \frac{\text{Massa (gram)}}{\text{Ar atau Mr}} \quad \text{atau} \quad \text{Massa} = n \times \text{Mr}")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Hitunglah jumlah mol dari 31,5 gram $\text{HNO}_3$! (Ar H=1, N=14, O=16)")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"\text{Mr HNO}_3 = 1 + 14 + (3 \times 16) = 63")
            st.latex(r"n = \frac{31,5\text{ gram}}{63} = 0,5\text{ mol}")
            
        st.markdown("##### ✍️ Latihan Mandiri")
        st.write(r"Berapa massa dari 0,2 mol kalsium karbonat ($\text{CaCO}_3$)? (Ar Ca=40, C=12, O=16)")
        st.text_input("Tulis jawabanmu (contoh: 20 gram):", key="l2_m1")
        st.write("---")

        # --- 2. Mol dan Jumlah Partikel ---
        st.subheader("2. Hubungan Mol dengan Jumlah Partikel")
        st.write("Satu mol zat mengandung partikel sebanyak Bilangan Avogadro ($L = 6,02 \times 10^{23}$).")
        st.latex(r"n = \frac{\text{Jumlah Partikel}}{6,02 \times 10^{23}} \quad \text{atau} \quad \text{Jumlah Partikel} = n \times (6,02 \times 10^{23})")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa jumlah atom Besi ($\text{Fe}$) dalam 0,1 mol paku besi?")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"\text{Jumlah atom} = 0,1 \times (6,02 \times 10^{23}) = 6,02 \times 10^{22} \text{ atom}")

        st.markdown("##### ✍️ Latihan Mandiri")
        st.write(r"Suatu sampel mengandung $3,01 \times 10^{23}$ molekul air. Berapa mol air tersebut?")
        st.text_input("Tulis jawabanmu (contoh: 0,5 mol):", key="l2_m2")
        st.write("---")

        # --- 3. Mol dan Volume Gas ---
        st.subheader("3. Hubungan Mol dengan Volume Gas")
        st.write("Volume gas sangat bergantung pada suhu (T) dan tekanan (P). Ada 3 kondisi utama:")
        st.markdown("**A. Keadaan Standar / STP (0°C, 1 atm)**")
        st.latex(r"\text{Volume}_{STP} = n \times 22,4\text{ L/mol}")
        st.markdown("**B. Keadaan Ruang / RTP (25°C, 1 atm)**")
        st.latex(r"\text{Volume}_{RTP} = n \times 24\text{ L/mol}")
        st.markdown("**C. Gas Ideal (Suhu & Tekanan Tertentu)**")
        st.latex(r"P \times V = n \times R \times T")
        st.caption("P = Tekanan (atm), V = Volume (L), R = 0,082 L.atm/mol.K, T = Suhu (Kelvin = °C + 273)")
        
        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa volume 8 gram gas $\text{CH}_4$ (Mr=16) pada suhu 27°C dan tekanan 1 atm? (R=0,082)")
        with st.expander("Lihat Pembahasan"):
            st.write("Langkah 1: Ubah massa ke mol (Jembatan Mol).")
            st.latex(r"n = \frac{8\text{ g}}{16} = 0,5\text{ mol}")
            st.write("Langkah 2: Gunakan rumus Gas Ideal ($T = 27 + 273 = 300\text{ K}$).")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{0,5 \times 0,082 \times 300}{1} = 12,3\text{ Liter}")

        st.markdown("##### ✍️ Latihan Mandiri")
        st.write("Berapa volume dari 0,2 mol gas oksigen pada keadaan STP?")
        st.text_input("Tulis jawabanmu (contoh: 4,48 Liter):", key="l2_m3")
        st.write("---")

        # --- 4. Mol dan Molaritas ---
        st.subheader("4. Hubungan Mol dengan Molaritas (Konsentrasi Larutan)")
        st.write("Molaritas (M) menyatakan jumlah mol zat terlarut dalam tiap 1 Liter larutan.")
        st.latex(r"M = \frac{n}{V\text{ (Liter)}} \quad \text{atau} \quad n = M \times V\text{ (Liter)}")

        st.markdown("##### 📝 Latihan Soal + Pembahasan")
        st.write(r"Berapa Molaritas larutan jika 4 gram $\text{NaOH}$ (Mr=40) dilarutkan dalam air hingga volumenya 500 mL?")
        with st.expander("Lihat Pembahasan"):
            st.latex(r"n = \frac{4\text{ g}}{40} = 0,1\text{ mol} \quad \text{dan} \quad V = 500\text{ mL} = 0,5\text{ L}")
            st.latex(r"M = \frac{0,1\text{ mol}}{0,5\text{ L}} = 0,2\text{ Molar}")

        st.write("---")

        # --- 5. Stoikiometri Senyawa ---
        st.subheader("5. Stoikiometri Senyawa (Kadar & Rumus Empiris)")
        st.write("**A. Kadar Unsur dalam Senyawa:**")
        st.latex(r"\% \text{Unsur} = \frac{\text{Jumlah atom} \times \text{Ar}}{\text{Mr Senyawa}} \times 100\%")
        st.write("**B. Rumus Empiris (RE) & Rumus Molekul (RM):**")
        st.info("Rumus Empiris adalah perbandingan mol paling sederhana dari unsur-unsur pembentuk senyawa. \nRumus Molekul adalah $(RE)_n = Mr$.")

    with tab_kuis:
        st.subheader("✍️ Kuis Evaluasi Level 2 (15 Soal Komprehensif)")
        st.write("Syarat lulus: Minimal benar 12 soal (Skor KKM: 80).")
        st.write("---")
        
        st.markdown("**Bagian 1: Konsep Mol Dasar (Massa & Partikel)**")
        q1 = st.radio("1. Jika Ar Fe=56, berapakah massa dari 0,5 mol logam besi?", ["28 gram", "56 gram", "112 gram", "14 gram"], key="l2q1")
        q2 = st.radio("2. Berapakah jumlah mol dari 9,8 gram H2SO4? (Mr = 98)", ["0,01 mol", "0,1 mol", "1 mol", "10 mol"], key="l2q2")
        q3 = st.radio("3. Satu mol suatu senyawa selalu mengandung...", ["Satu gram zat", "22,4 Liter pada suhu berapapun", "6,02 x 10^23 partikel", "Massa yang sama dengan air"], key="l2q3")
        q4 = st.radio("4. Berapa jumlah molekul yang terdapat dalam 0,2 mol gas O2?", ["1,204 x 10^23 molekul", "3,01 x 10^23 molekul", "6,02 x 10^22 molekul", "1,204 x 10^22 molekul"], key="l2q4")
        q5 = st.radio("5. Suatu sampel mengandung 3,01 x 10^23 atom Karbon. Berapakah massa sampel tersebut? (Ar C=12)", ["3 gram", "6 gram", "12 gram", "24 gram"], key="l2q5")

        st.markdown("**Bagian 2: Jembatan Mol (Volume & Molaritas)**")
        q6 = st.radio("6. Berapa volume dari 0,5 mol gas N2 pada keadaan STP (0°C, 1 atm)?", ["11,2 L", "22,4 L", "5,6 L", "44,8 L"], key="l2q6")
        q7 = st.radio("7. Jika volume gas CO2 pada keadaan RTP (25°C, 1 atm) adalah 12 Liter, berapa mol gas tersebut?", ["0,2 mol", "0,5 mol", "1 mol", "2 mol"], key="l2q7")
        q8 = st.radio("8. Massa dari 5,6 Liter gas SO2 pada keadaan STP adalah... (Ar S=32, O=16, Mr=64)", ["8 gram", "16 gram", "32 gram", "64 gram"], key="l2q8")
        q9 = st.radio("9. Jika 2 mol gas O2 berada dalam tabung pada suhu 27°C (300K) dan tekanan 2 atm (R=0,082), volumenya adalah...", ["12,3 L", "24,6 L", "30 L", "49,2 L"], key="l2q9")
        q10 = st.radio("10. Sebanyak 5,85 gram NaCl (Mr=58,5) dilarutkan dalam air hingga volumenya 250 mL. Molaritas larutan tersebut adalah...", ["0,1 M", "0,2 M", "0,4 M", "1,0 M"], key="l2q10")

        st.markdown("**Bagian 3: Stoikiometri Senyawa & Campuran**")
        q11 = st.radio("11. Berapakah persentase massa unsur Karbon (Ar C=12) dalam senyawa CO(NH2)2 (Mr=60)?", ["12%", "20%", "24%", "40%"], key="l2q11")
        q12 = st.radio("12. Suatu senyawa memiliki rumus empiris CH2. Jika Mr senyawa tersebut adalah 42, maka rumus molekulnya adalah... (Ar C=12, H=1)", ["C2H4", "C3H6", "C4H8", "C5H10"], key="l2q12")
        q13 = st.radio("13. Senyawa hidrokarbon mengandung 80% Karbon dan 20% Hidrogen. Rumus empirisnya adalah... (Ar C=12, H=1)", ["CH2", "CH3", "C2H4", "C2H6"], key="l2q13")
        q14 = st.radio("14. Volume larutan HCl 0,2 M yang mengandung 0,1 mol HCl adalah...", ["200 mL", "250 mL", "500 mL", "1000 mL"], key="l2q14")
        q15 = st.radio("15. [Tantangan] Massa 3,01 x 10^23 molekul gas X adalah 22 gram. Berapakah volume gas X tersebut pada keadaan STP?", ["5,6 Liter", "11,2 Liter", "22,4 Liter", "44,8 Liter"], key="l2q15")

        st.write("---")
        if st.button("Kirim Lembar Jawaban Level 2 📝"):
            jawaban_benar = 0
            if q1 == "28 gram": jawaban_benar += 1
            if q2 == "0,1 mol": jawaban_benar += 1
            if q3 == "6,02 x 10^23 partikel": jawaban_benar += 1
            if q4 == "1,204 x 10^23 molekul": jawaban_benar += 1
            if q5 == "6 gram": jawaban_benar += 1
            if q6 == "11,2 L": jawaban_benar += 1
            if q7 == "0,5 mol": jawaban_benar += 1
            if q8 == "16 gram": jawaban_benar += 1
            if q9 == "24,6 L": jawaban_benar += 1
            if q10 == "0,4 M": jawaban_benar += 1
            if q11 == "20%": jawaban_benar += 1
            if q12 == "C3H6": jawaban_benar += 1
            if q13 == "CH3": jawaban_benar += 1
            if q14 == "500 mL": jawaban_benar += 1
            if q15 == "11,2 Liter": jawaban_benar += 1
            
            skor = round((jawaban_benar / 15) * 100)
            
            if skor >= 80:
                st.session_state.level_3_terbuka = True
                st.success(f"🎉 LULUS! Kamu benar {jawaban_benar} dari 15 soal. Skor kamu: {skor}. Kunci Level 3 resmi DIBUKA!")
                st.balloons()
            else:
                st.error(f"❌ BELUM LULUS! Kamu baru benar {jawaban_benar} dari 15 soal. Skor kamu: {skor} (KKM: 80). Silakan baca lagi peta Jembatan Mol di pembahasan!")
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Lengkap")
            
            st.info("1. **28 gram**")
            st.latex(r"\text{Massa} = 0,5\text{ mol} \times 56 = 28\text{ g}")
            
            st.info("2. **0,1 mol**")
            st.latex(r"n = \frac{9,8\text{ g}}{98} = 0,1\text{ mol}")
            
            st.info("3. **6,02 x 10^23 partikel** (Definisi tetapan Avogadro)")
            
            st.info("4. **1,204 x 10^23 molekul**")
            st.latex(r"\text{Molekul} = 0,2 \times (6,02 \times 10^{23}) = 1,204 \times 10^{23}")
            
            st.info("5. **6 gram**")
            st.latex(r"n = \frac{3,01 \times 10^{23}}{6,02 \times 10^{23}} = 0,5\text{ mol}. \quad \text{Massa} = 0,5 \times 12 = 6\text{ g}")
            
            st.info("6. **11,2 L**")
            st.latex(r"V = 0,5\text{ mol} \times 22,4 = 11,2\text{ L}")
            
            st.info("7. **0,5 mol**")
            st.latex(r"n = \frac{12\text{ L}}{24\text{ (RTP)}} = 0,5\text{ mol}")
            
            st.info("8. **16 gram**")
            st.latex(r"n = \frac{5,6}{22,4} = 0,25\text{ mol}. \quad \text{Massa} = 0,25 \times 64 = 16\text{ g}")
            
            st.info("9. **24,6 L** (Gas Ideal)")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{2 \times 0,082 \times 300}{2} = 24,6\text{ L}")
            
            st.info("10. **0,4 M**")
            st.latex(r"n = \frac{5,85}{58,5} = 0,1\text{ mol}. \quad M = \frac{0,1\text{ mol}}{0,25\text{ L}} = 0,4\text{ M}")

            st.info("11. **20%**")
            st.latex(r"\% C = \frac{1 \times 12}{60} \times 100\% = 20\%")
            
            st.info("12. **C3H6**")
            st.latex(r"(\text{CH}_2)_n = 42 \implies (12 + 2)_n = 42 \implies 14n = 42 \implies n = 3")
            
            st.info("13. **CH3**")
            st.latex(r"\text{Mol C} : \text{Mol H} = \frac{80}{12} : \frac{20}{1} = 6,67 : 20 = 1 : 3")
            
            st.info("14. **500 mL**")
            st.latex(r"V = \frac{n}{M} = \frac{0,1}{0,2} = 0,5\text{ L} = 500\text{ mL}")
            
            st.info("15. **11,2 Liter** (Jembatan Mol Ekstra)")
            st.write("Partikel -> Mol -> Volume STP")
            st.latex(r"n = \frac{3,01 \times 10^{23}}{6,02 \times 10^{23}} = 0,5\text{ mol}. \quad V = 0,5 \times 22,4 = 11,2\text{ Liter}")
            
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
    
