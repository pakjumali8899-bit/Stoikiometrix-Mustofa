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
 elif st.session_state.get('menu_aktif') == 'level_2':
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 2: Konsep Mol & Stoikiometri Senyawa")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi Pembelajaran", "✍️ Kuis Evaluasi Level 2"])

    with tab_materi:
        # --- Bagian A: Pengantar Konsep Mol ---
        st.header("A. Pengantar Konsep Mol")
        st.write("Dalam kehidupan sehari-hari, kita menggunakan satuan lusin untuk menyatakan isi 12 buah benda. Karena atom dan molekul memiliki ukuran yang luar biasa kecil, para ilmuwan kimia memerlukan satuan khusus yang dinamakan **Mol**.")
        st.write("**Mol** adalah satuan internasional (SI) untuk menyatakan jumlah zat. Satu mol zat apa pun akan selalu mengandung jumlah partikel yang sama banyak dengan jumlah atom dalam 12 gram Karbon-12.")
        
        # --- Bagian B: Jembatan Mol ---
        st.header("B. Jembatan Mol")
        st.write("Jembatan Mol adalah sebuah peta konsep terpusat yang menghubungkan satuan Mol dengan tiga dimensi ukuran kimia lainnya: Massa (gram), Jumlah Partikel, Volume Gas, dan Molaritas Larutan.")
        try:
            st.image("konsep_mol.gif", caption="Peta Terminal Jembatan Mol", use_container_width=True)
        except:
            st.info("💡 Catatan: Pastikan file 'konsep_mol.gif' sudah ada di folder utama GitHub kamu.")
            
        st.write("---")

        # --- 1. Hubungan Mol dengan Massa ---
        st.subheader("1. Hubungan Mol dengan Massa (Massa Molar)")
        st.write("Massa molar ($Ar$ untuk unsur atau $Mr$ untuk senyawa) menyatakan massa dalam satuan gram untuk setiap 1 mol zat.")
        st.markdown("**🔄 Rumus Bolak-Balik:**")
        st.write("Mencari Jumlah Mol:")
        st.latex(r"n = \frac{\text{Massa (gram)}}{\text{Ar atau Mr}}")
        st.write("Mencari Massa Zat:")
        st.latex(r"\text{Massa (gram)} = n \times \text{(Ar atau Mr)}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Hitunglah jumlah mol yang terkandung di dalam 12,6 gram asam nitrat ($\text{HNO}_3$) jika diketahui $Ar\text{ H}=1, \text{N}=14, \text{O}=16$!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Hitung massa molekul relatif ($Mr$) dari senyawa $\text{HNO}_3$:")
            st.latex(r"\text{Mr HNo}_3 = (1 \times 1) + (1 \times 14) + (3 \times 16) = 63 \text{ g/mol}")
            st.write("Langkah 2: Gunakan rumus pecahan untuk mencari mol ($n$):")
            st.latex(r"n = \frac{12,6 \text{ gram}}{63 \text{ g/mol}} = 0,2 \text{ mol}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Berapakah total massa dari 0,3 mol senyawa kalsium fosfat $\text{Ca}_3(\text{PO}_4)_2$? (Diketahui $Ar\text{ Ca}=40, \text{P}=31, \text{O}=16$)")
        st.write("---")

        # --- 2. Hubungan Mol dengan Jumlah Partikel ---
        st.subheader("2. Hubungan Mol dengan Jumlah Partikel")
        st.write("Satu mol zat mengandung jumlah partikel sebanyak Bilangan Avogadro ($6,02 \times 10^{23}$ partikel). Partikel di sini bisa berwujud atom, molekul, ataupun ion.")
        st.markdown("**🔄 Rumus Bolak-Balik:**")
        st.write("Mencari Jumlah Mol:")
        st.latex(r"n = \frac{X}{6,02 \times 10^{23}}")
        st.write("Mencari Jumlah Partikel ($X$):")
        st.latex(r"X = n \times 6,02 \times 10^{23}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Sebuah paku besi murni mengandung sebanyak $3,01 \times 10^{22}$ atom besi ($\text{Fe}$). Tentukan jumlah mol besi di dalam paku tersebut!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Masukkan nilai jumlah atom ke dalam rumus pembagian konversi partikel:")
            st.latex(r"n = \frac{3,01 \times 10^{22}}{6,02 \times 10^{23}} = 0,05 \text{ mol}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Hitunglah berapa total jumlah molekul gas amonia yang terkandung di dalam suatu wadah tertutup berisi 2,5 mol gas $\text{NH}_3$!")
        st.write("---")

        # --- 3. Hubungan Mol dengan Volume Gas ---
        st.subheader("3. Hubungan Mol dengan Volume Gas")
        st.write("Volume gas sangat dipengaruhi oleh variabel suhu ($T$) dan tekanan ($P$). Berikut adalah 4 kondisi formulasinya:")
        
        st.markdown("**A. Keadaan Standar / STP (Suhu 0°C, Tekanan 1 atm)**")
        st.latex(r"V_{\text{STP}} = n \times 22,4 \quad \iff \quad n = \frac{V_{\text{STP}}}{22,4}")
        
        st.markdown("**B. Keadaan Kamar / RTP (Suhu 25°C, Tekanan 1 atm)**")
        st.latex(r"V_{\text{RTP}} = n \times 24 \quad \iff \quad n = \frac{V_{\text{RTP}}}{24}")
        
        st.markdown("**C. Persamaan Gas Ideal (Suhu & Tekanan Spesifik)**")
        st.latex(r"P \times V = n \times R \times T \quad \iff \quad V = \frac{n \times R \times T}{P}")
        st.caption("$P$ = tekanan (atm), $V$ = volume gas (L), $R$ = tetapan gas ideal (0,082 L.atm/mol.K), $T$ = suhu mutlak (Kelvin = °C + 273)")
        
        st.markdown("**D. Kondisi Dua Gas Berbeda (Suhu & Tekanan Sama)**")
        st.latex(r"\frac{V_1}{V_2} = \frac{n_1}{n_2}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Hitunglah volume dari 4,4 gram gas karbondioksida ($\text{CO}_2$, $Mr = 44$) jika diukur pada kondisi suhu 27°C dan tekanan 2 atm!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Cari nilai mol gas $\text{CO}_2$ terlebih dahulu:")
            st.latex(r"n = \frac{4,4 \text{ gram}}{44 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Langkah 2: Konversikan satuan suhu Celcius menjadi Kelvin:")
            st.latex(r"T = 27 + 273 = 300 \text{ K}")
            st.write("Langkah 3: Masukkan komponen data ke dalam pecahan hukum gas ideal:")
            st.latex(r"V = \frac{0,1 \times 0,082 \times 300}{2} = 1,23 \text{ Liter}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Pada suhu dan tekanan tertentu, 1 mol gas nitrogen ($\text{N}_2$) memiliki volume 15 Liter. Pada kondisi lingkungan yang sama, berapakah volume dari 0,4 mol gas oksigen ($\text{O}_2$)?")
        st.write("---")

        # --- 4. Hubungan Mol dengan Molaritas Larutan ---
        st.subheader("4. Hubungan Mol dengan Molaritas (Konsentrasi Larutan)")
        st.write("Molaritas ($M$) menyatakan tolok ukur kepekatan larutan yang dinilai dari banyaknya mol zat terlarut dalam tiap satu Liter volume larutan.")
        st.markdown("**🔄 Rumus Bolak-Balik:**")
        st.write("Mencari Molaritas:")
        st.latex(r"M = \frac{n}{V_{\text{Liter}}}")
        st.write("Mencari Jumlah Mol:")
        st.latex(r"n = M \times V_{\text{Liter}}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Sebanyak 4 gram kristal natrium hidroksida ($\text{NaOH}$, $Mr = 40$) dilarutkan ke dalam air hingga volume larutan mencapai 250 mL. Berapakah Molaritas larutan yang terbentuk?")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Hitung jumlah mol dari zat terlarut $\text{NaOH}$:")
            st.latex(r"n = \frac{4 \text{ gram}}{40 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Langkah 2: Ubah satuan volume larutan mililiter menjadi Liter:")
            st.latex(r"V = \frac{250 \text{ mL}}{1000} = 0,25 \text{ Liter}")
            st.write("Langkah 3: Hitung konsentrasi Molaritasnya:")
            st.latex(r"M = \frac{0,1 \text{ mol}}{0,25 \text{ Liter}} = 0,4 \text{ M}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Berapa gram kristal garam $\text{NaCl}$ ($Mr = 58,5$) yang harus ditimbang untuk membuat larutan garam dapur ber-konsentrasi 0,2 M dengan volume tepat 500 mL?")

    with tab_kuis:
        st.subheader("✍️ Kuis Akhir Komprehensif Level 2")
        st.write("Kerjakan 15 soal di bawah ini dengan cermat untuk mengevaluasi pemahamanmu secara menyeluruh.")
        st.write("---")
        
        q1 = st.radio("1. Massa dari 2 mol molekul air (H2O, Mr = 18) adalah...", ["18 gram", "36 gram", "9 gram", "54 gram"], key="k2_q1")
        q2 = st.radio("2. Jumlah mol atom Karbon yang terdapat di dalam 12 gram sampel karbon murni (Ar C = 12) adalah...", ["0,5 mol", "1 mol", "2 mol", "12 mol"], key="k2_q2")
        q3 = st.radio("3. Berapakah jumlah atom total yang terdapat di dalam 0,5 mol logam Tembaga (Cu)?", ["3,01 x 10^23 atom", "6,02 x 10^23 atom", "1,204 x 10^24 atom", "3,01 x 10^22 atom"], key="k2_q3")
        q4 = st.radio("4. Suatu sampel gas mengandung 1,204 x 10^24 molekul CO2. Jumlah mol gas tersebut adalah...", ["0,5 mol", "1 mol", "2 mol", "4 mol"], key="k2_q4")
        q5 = st.radio("5. Jika massa dari 3,01 x 10^23 atom suatu logam murni adalah 28 gram, berapakah Ar logam tersebut?", ["14 g/mol", "28 g/mol", "56 g/mol", "112 g/mol"], key="k2_q5")
        q6 = st.radio("6. Berapakah volume dari 0,25 mol gas oksigen (O2) jika diukur pada keadaan standar (STP)?", ["2,8 Liter", "5,6 Liter", "11,2 Liter", "22,4 Liter"], key="k2_q6")
        q7 = st.radio("7. Gas metana (CH4, Mr = 16) bermassa 8 gram jika diukur pada kondisi kamar (RTP) memiliki volume sebesar...", ["5,6 Liter", "11,2 Liter", "12 Liter", "24 Liter"], key="k2_q7")
        q8 = st.radio("8. Hitunglah volume dari 0,5 mol gas ideal yang berada dalam wadah bersuhu 27°C (300 K) bertekanan 1 atm! (R = 0,082)", ["11,2 Liter", "12,3 Liter", "22,4 Liter", "24,6 Liter"], key="k2_q8")
        q9 = st.radio("9. Pada suhu dan tekanan tertentu, 2 mol gas O2 bervolume 10 Liter. Pada kondisi lingkungan yang sama, volume dari 4 mol gas CO2 adalah...", ["5 Liter", "10 Liter", "20 Liter", "40 Liter"], key="k2_q9")
        q10 = st.radio("10. Jika 4,48 Liter gas N2 pada keadaan STP ditimbang, berapakah massa gas tersebut? (Mr N2 = 28)", ["2,8 gram", "5,6 gram", "7 gram", "14 gram"], key="k2_q10")
        q11 = st.radio("11. Sebanyak 0,1 mol asam klorida (HCl) dilarutkan ke dalam air hingga volume 500 mL. Berapakah molaritas larutan?", ["0,05 M", "0,1 M", "0,2 M", "0,5 M"], key="k2_q11")
        q12 = st.radio("12. Larutan NaOH dengan konsentrasi 0,4 M mengandung zat terlarut sebanyak 0,1 mol. Berapakah volume larutan tersebut?", ["100 mL", "250 mL", "400 mL", "500 mL"], key="k2_q12")
        q13 = st.radio("13. Berapakah jumlah partikel molekul yang ada di dalam 11,2 Liter gas ideal pada kondisi STP?", ["1,505 x 10^23", "3,01 x 10^23", "6,02 x 10^23", "1,204 x 10^24"], key="k2_q13")
        q14 = st.radio("14. Massa dari 1 mol gas ideal X2 pada STP adalah 32 gram. Unsur X yang dimaksud adalah...", ["Hidrogen (Ar=1)", "Karbon (Ar=12)", "Nitrogen (Ar=14)", "Oksigen (Ar=16)"], key="k2_q14")
        q15 = st.radio("15. Larutan garam dapur dibuat dengan melarutkan 5,85 gram NaCl (Mr = 58,5) ke dalam air hingga volume 1 Liter. Konsentrasi larutan tersebut adalah...", ["0,01 M", "0,1 M", "0,5 M", "1,0 M"], key="k2_q15")

        st.write("---")
        if st.button("Periksa Hasil Jawaban & Lihat Pembahasan Level 2 📝"):
            skor_hitung = 0
            if q1 == "36 gram": skor_hitung += 1
            if q2 == "1 mol": skor_hitung += 1
            if q3 == "3,01 x 10^23 atom": skor_hitung += 1
            if q4 == "2 mol": skor_hitung += 1
            if q5 == "56 g/mol": skor_hitung += 1
            if q6 == "5,6 Liter": skor_hitung += 1
            if q7 == "12 Liter": skor_hitung += 1
            if q8 == "12,3 Liter": skor_hitung += 1
            if q9 == "20 Liter": skor_hitung += 1
            if q10 == "5,6 gram": skor_hitung += 1
            if q11 == "0,2 M": skor_hitung += 1
            if q12 == "250 mL": skor_hitung += 1
            if q13 == "3,01 x 10^23": skor_hitung += 1
            if q14 == "Oksigen (Ar=16)": skor_hitung += 1
            if q15 == "0,1 M": skor_hitung += 1
            
            skor_final = round((skor_hitung / 15) * 100)
            st.success(f"Evaluasi selesai! Kamu menjawab {skor_hitung} dari 15 soal dengan benar. Skor kamu: {skor_final} / 100.")
            st.balloons()
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Detil:")
            
            st.markdown("**Soal 1**")
            st.latex(r"\text{Massa} = n \times Mr = 2 \text{ mol} \times 18 \text{ g/mol} = 36 \text{ gram}")
            
            st.markdown("**Soal 2**")
            st.latex(r"n = \frac{\text{Massa}}{Ar} = \frac{12 \text{ gram}}{12 \text{ g/mol}} = 1 \text{ mol}")
            
            st.markdown("**Soal 3**")
            st.latex(r"X = n \times 6,02 \times 10^{23} = 0,5 \times 6,02 \times 10^{23} = 3,01 \times 10^{23} \text{ atom}")
            
            st.markdown("**Soal 4**")
            st.latex(r"n = \frac{1,204 \times 10^{24}}{6,02 \times 10^{23}} = 2 \text{ mol}")
            
            st.markdown("**Soal 5**")
            st.write("Jumlah mol ($n$):")
            st.latex(r"n = \frac{3,01 \times 10^{23}}{6,02 \times 10^{23}} = 0,5 \text{ mol}")
            st.write("Massa atom relatif ($Ar$):")
            st.latex(r"Ar = \frac{\text{Massa}}{n} = \frac{28 \text{ gram}}{0,5 \text{ mol}} = 56 \text{ g/mol}")
            
            st.markdown("**Soal 6**")
            st.latex(r"V_{\text{STP}} = n \times 22,4 = 0,25 \times 22,4 = 5,6 \text{ Liter}")
            
            st.markdown("**Soal 7**")
            st.write("Jumlah mol ($n$):")
            st.latex(r"n = \frac{8 \text{ gram}}{16 \text{ g/mol}} = 0,5 \text{ mol}")
            st.write("Volume keadaan kamar ($RTP$):")
            st.latex(r"V_{\text{RTP}} = n \times 24 = 0,5 \times 24 = 12 \text{ Liter}")
            
            st.markdown("**Soal 8**")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{0,5 \times 0,082 \times 300}{1} = 12,3 \text{ Liter}")
            
            st.markdown("**Soal 9**")
            st.write("Pada kondisi suhu dan tekanan tetap, perbandingan volume sebanding dengan mol:")
            st.latex(r"V_2 = \frac{n_2}{n_1} \times V_1 = \frac{4 \text{ mol}}{2 \text{ mol}} \times 10 \text{ L} = 20 \text{ Liter}")
            
            st.markdown("**Soal 10**")
            st.write("Jumlah mol ($n$):")
            st.latex(r"n = \frac{4,48 \text{ L}}{22,4 \text{ L/mol}} = 0,2 \text{ mol}")
            st.write("Massa gas:")
            st.latex(r"\text{Massa} = 0,2 \text{ mol} \times 28 \text{ g/mol} = 5,6 \text{ gram}")
            
            st.markdown("**Soal 11**")
            st.latex(r"M = \frac{n}{V} = \frac{0,1 \text{ mol}}{0,5 \text{ Liter}} = 0,2 \text{ M}")
            
            st.markdown("**Soal 12**")
            st.latex(r"V = \frac{n}{M} = \frac{0,1 \text{ mol}}{0,4 \text{ M}} = 0,25 \text{ Liter} = 250 \text{ mL}")
            
            st.markdown("**Soal 13**")
            st.write("Jumlah mol ($n$):")
            st.latex(r"n = \frac{11,2 \text{ L}}{22,4 \text{ L/mol}} = 0,5 \text{ mol}")
            st.write("Jumlah partikel ($X$):")
            st.latex(r"X = 0,5 \times 6,02 \times 10^{23} = 3,01 \times 10^{23} \text{ molekul}")
            
            st.markdown("**Soal 14**")
            st.write("Karena 1 mol bermassa 32 gram, maka $Mr\text{ X}_2 = 32$. Maka $Ar\text{ X} = 16$ (Oksigen).")
            
            st.markdown("**Soal 15**")
            st.write("Jumlah mol ($n$):")
            st.latex(r"n = \frac{5,85 \text{ gram}}{58,5 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Molaritas larutan:")
            st.latex(r"M = \frac{0,1 \text{ mol}}{1 \text{ Liter}} = 0,1 \text{ M}")
            
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
    
