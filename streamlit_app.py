import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Stoikiometrix by Mustofa", page_icon="🧪")

# --- INISIALISASI STATUS LOGIN & MENU ---
if 'sudah_login' not in st.session_state:
    st.session_state.sudah_login = False

if 'menu_aktif' not in st.session_state:
    st.session_state.menu_aktif = 'dashboard'

if 'nama_user' not in st.session_state:
    st.session_state.nama_user = ""

# --- PENGATURAN TOKEN RAHASIA ---
TOKEN_AKSES = "54321"

# --- 1. TAMPILAN HALAMAN LOGIN (JIKA BELUM LOGIN) ---
if not st.session_state.sudah_login:
    st.markdown("""
        <style>
        @keyframes gradient-gerak {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .judul-kece {
            font-size: 45px;
            font-weight: 800;
            background: linear-gradient(-45deg, #ff4b4b, #ff8585, #4b92ff, #2b5cff);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-color: transparent;
            -webkit-text-fill-color: transparent;
            animation: gradient-gerak 4s ease infinite;
            display: inline-block;
        }
        .sub-flat {
            font-size: 20px;
            color: #666666;
            font-weight: 400;
            margin-left: 10px;
            vertical-align: middle;
        }
        </style>
        <div>
            <span class="judul-kece">Stoikiometrix</span>
            <span class="sub-flat">by Mustofa</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("Silakan masukkan nama dan token untuk mengakses aplikasi pembelajaran.")
    
    nama_input = st.text_input("Nama Lengkap:", placeholder="Ketik nama kamu di sini...")
    token_input = st.text_input("Token Akses:", type="password")
    
    if st.button("Masuk 🚀"):
        if not nama_input.strip():
            st.error("❌ Nama lengkap wajib diisi!")
        elif token_input == TOKEN_AKSES:
            st.session_state.sudah_login = True
            st.session_state.nama_user = nama_input
            st.success("Token benar! Selamat belajar.")
            st.rerun()
        else:
            st.error("❌ Token yang kamu masukkan salah. Coba lagi ya!")

# --- 2. TAMPILAN DASHBOARD UTAMA (JIKA SUDAH LOGIN & DI MENU DASHBOARD) ---
elif st.session_state.sudah_login and (st.session_state.menu_aktif == 'dashboard' or st.session_state.menu_aktif is None):
    st.success(f"Selamat datang kembali, {st.session_state.nama_user}! 🎉")
    st.title("🧪 Dashboard Utama")
    st.write("Silakan pilih level pembelajaran di bawah ini:")

    if 'level_2_terbuka' not in st.session_state:
        st.session_state.level_2_terbuka = False
    if 'level_3_terbuka' not in st.session_state:
        st.session_state.level_3_terbuka = False

    if st.button("🚀 Masuk ke Level 1: Hukum Dasar Kimia"):
        st.session_state.menu_aktif = 'level_1'
        st.rerun()
        
    if st.button("🎮 Masuk ke Level 2: Konsep Mol & Stoikiometri"):
        st.session_state.menu_aktif = 'level_2'
        st.rerun()
        
    if st.button("🔥 Masuk ke Level 3: Perhitungan Persamaan Reaksi"):
        st.session_state.menu_aktif = 'level_3'
        st.rerun()

    # TOMBOL KELUAR HANYA ADA DI SINI (Muncul hanya jika sudah sukses login)
    st.write("---")
    if st.button("🚪 Keluar / Logout"):
        st.session_state.sudah_login = False
        st.session_state.menu_aktif = 'dashboard'
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
    # --- TOMBOL KEMBALI KE DASHBOARD ---
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🧪 Level 2: Konsep Mol & Stoikiometri Senyawa")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi Pembelajaran", "✍️ Kuis Evaluasi Level 2"])

    with tab_materi:
        # --- Bagian A: Pengantar Konsep Mol ---
        st.header("A. Pengantar Konsep Mol")
        st.write("Dalam kehidupan sehari-hari, kita terbiasa menggunakan satuan kelompok untuk menghitung jumlah benda yang banyak. Misalnya, satuan **lusin** untuk menyatakan isi 12 buah benda, atau **kodi** untuk menyatakan 20 lembar pakaian.")
        st.write("Di dalam laboratorium kimia, para ilmuwan menghadapi miliaran atom atau molekul yang ukurannya luar biasa kecil. Menghitungnya satu per satu tentu mustahil. Oleh karena itu, ditetapkanlah sebuah satuan khusus yang dinamakan **Mol**.")
        st.write("**Mol** adalah satuan internasional (SI) yang menyatakan jumlah zat. Satu mol zat apa pun (baik itu air, emas, maupun gas oksigen) akan selalu mengandung jumlah partikel yang sama banyak dengan jumlah atom dalam tepat 12 gram Karbon-12.")
        
        # --- Bagian B: Peta Jembatan Mol ---
        st.header("B. Terminal Jembatan Mol")
        st.write("Jembatan Mol adalah peta konsep utama yang memposisikan satuan **Mol** sebagai pusat terminal perhitungan. Segala macam konversi satuan dalam kuantitas kimia harus melewati terminal Mol ini terlebih dahulu sebelum bisa diubah ke satuan lain.")
        try:
            st.image("konsep_mol.gif", use_container_width=True)
            st.caption("📷 **Peta Terminal Utama Jembatan Mol** | *Sumber gambar: [Nixon Selly - Konsep Mol dan Stoikiometri](https://nixonselly.blogspot.com/2019/01/konsep-mol-dan-stoikiometri.html)*")
        except:
            st.info("💡 Catatan Visual: Pastikan file 'konsep_mol.gif' sudah tersedia di repositori utama GitHub kamu.")
            
        st.write("---")

        # --- 1. Hubungan Mol dengan Massa ---
        st.subheader("1. Hubungan Mol dengan Massa (Massa Molar)")
        st.write("Massa molar menyatakan massa dalam satuan gram untuk setiap 1 mol zat. Nilai massa molar ini sama dengan Massa Atom Relatif (Ar) untuk unsur, atau Massa Molekul Relatif (Mr) untuk senyawa.")
        
        st.markdown("**🔄 Rumus Konversi Murni (Atas-Bawah):**")
        st.write("Jika ingin mencari Jumlah Mol (n):")
        st.latex(r"n = \frac{\text{Massa (gram)}}{\text{Ar atau Mr}}")
        st.write("Jika ingin mencari Massa Zat (gram):")
        st.latex(r"\text{Massa (gram)} = n \times \text{(Ar atau Mr)}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Hitunglah jumlah mol yang terkandung di dalam 12,6 gram asam nitrat (HNO₃) jika diketahui Ar H = 1, N = 14, O = 16!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Hitung massa molekul relatif (Mr) total dari senyawa HNO₃:")
            st.latex(r"\text{Mr HNO}_3 = (1 \times 1) + (1 \times 14) + (3 \times 16) = 63 \text{ g/mol}")
            st.write("Langkah 2: Masukkan ke dalam rumus pembagian untuk mencari mol:")
            st.latex(r"n = \frac{12,6 \text{ gram}}{63 \text{ g/mol}} = 0,2 \text{ mol}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Berapakah total massa dalam satuan gram dari 0,3 mol senyawa kalsium fosfat Ca₃(PO₄)₂? (Diketahui Ar Ca = 40, P = 31, O = 16)")
        st.write("---")

        # --- 2. Hubungan Mol dengan Jumlah Partikel ---
        st.subheader("2. Hubungan Mol dengan Jumlah Partikel (Bilangan Avogadro)")
        st.write("Berdasarkan penelitian, didapatkan bahwa 1 mol zat mengandung jumlah partikel sebanyak 6,02 x 10²³ partikel. Angka konstan ini disebut sebagai Bilangan Avogadro (L). Partikel zat dapat berupa atom, molekul, ataupun gabungan ion.")
        
        st.markdown("**🔄 Rumus Konversi Murni (Atas-Bawah):**")
        st.write("Jika ingin mencari Jumlah Mol (n):")
        st.latex(r"n = \frac{X}{6,02 \times 10^{23}}")
        st.write("Jika ingin mencari Jumlah Partikel (X):")
        st.latex(r"X = n \times 6,02 \times 10^{23}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Sebuah paku besi murni setelah dianalisis ternyata mengandung sebanyak 3,01 x 10²² atom besi (Fe). Tentukan jumlah mol besi di dalam paku tersebut!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Gunakan rumus pecahan pembagian konversi partikel ke terminal mol:")
            st.latex(r"n = \frac{3,01 \times 10^{22}}{6,02 \times 10^{23}} = 0,05 \text{ mol}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Hitunglah berapa total jumlah molekul gas amonia yang berterbangan di dalam suatu wadah tabung tertutup berisi 2,5 mol gas NH₃!")
        st.write("---")

        # --- 3. Hubungan Mol dengan Volume Gas ---
        st.subheader("3. Hubungan Mol dengan Volume Gas")
        st.write("Kerapatan gas sangat dipengaruhi oleh lingkungan suhu (T) dan tekanan (P). Oleh karena itu, perhitungan volume gas dibagi menjadi 4 jenis kondisi lingkungan:")
        
        st.markdown("**A. Keadaan Standar / STP (Suhu 0°C, Tekanan 1 atm)**")
        st.latex(r"V_{\text{STP}} = n \times 22,4 \quad \iff \quad n = \frac{V_{\text{STP}}}{22,4}")
        
        st.markdown("**B. Keadaan Kamar / RTP (Suhu 25°C, Tekanan 1 atm)**")
        st.latex(r"V_{\text{RTP}} = n \times 24 \quad \iff \quad n = \frac{V_{\text{RTP}}}{24}")
        
        st.markdown("**C. Persamaan Gas Ideal (Pada Suhu & Tekanan Tertentu)**")
        st.latex(r"P \times V = n \times R \times T \quad \iff \quad V = \frac{n \times R \times T}{P}")
        st.caption("P = tekanan (atm), V = volume (L), R = tetapan gas (0,082 L.atm/mol.K), T = suhu mutlak (Kelvin = °C + 273)")
        
        st.markdown("**D. Kondisi Dua Gas Berbeda (Diukur pada Suhu & Tekanan yang Sama)**")
        st.write("Sesuai Hukum Avogadro, perbandingan volume gas akan setara dengan perbandingan jumlah molnya:")
        st.latex(r"\frac{V_1}{V_2} = \frac{n_1}{n_2}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Hitunglah volume dari 4,4 gram gas karbondioksida (CO₂, Mr = 44) jika diukur pada kondisi suhu ruangan 27°C dan tekanan 2 atm!")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Ubah massa gas menjadi satuan mol terlebih dahulu:")
            st.latex(r"n = \frac{4,4 \text{ gram}}{44 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Langkah 2: Konversikan parameter suhu Celcius menjadi Kelvin mutlak:")
            st.latex(r"T = 27 + 273 = 300 \text{ K}")
            st.write("Langkah 3: Masukkan data ke pecahan rumus hukum gas ideal:")
            st.latex(r"V = \frac{0,1 \times 0,082 \times 300}{2} = 1,23 \text{ Liter}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Pada suhu dan tekanan tertentu, 1 mol gas nitrogen (N₂) memiliki volume 15 Liter. Pada kondisi lingkungan yang sama, berapakah volume dari 0,4 mol gas oksigen (O₂)?")
        st.write("---")

        # --- 4. Hubungan Mol dengan Molaritas Larutan ---
        st.subheader("4. Hubungan Mol dengan Molaritas (Konsentrasi Larutan)")
        st.write("Molaritas (M) adalah satuan kepekatan yang menyatakan banyaknya mol zat terlarut yang terkandung di dalam setiap satu Liter volume larutan.")
        
        st.markdown("**🔄 Rumus Konversi Murni (Atas-Bawah):**")
        st.write("Jika ingin mencari Molaritas (M):")
        st.latex(r"M = \frac{n}{V_{\text{Liter}}}")
        st.write("Jika ingin mencari Jumlah Mol (n):")
        st.latex(r"n = M \times V_{\text{Liter}}")
        
        st.markdown("**📝 Latihan Soal dengan Pembahasan:**")
        st.write("Sebanyak 4 gram kristal natrium hidroksida (NaOH, Mr = 40) dilarutkan ke dalam air hingga volume larutan mencapai 250 mL. Berapakah Molaritas larutan yang terbentuk?")
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Langkah 1: Hitung jumlah mol zat terlarut NaOH:")
            st.latex(r"n = \frac{4 \text{ gram}}{40 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Langkah 2: Ubah satuan volume larutan mililiter menjadi satuan Liter:")
            st.latex(r"V = \frac{250 \text{ mL}}{1000} = 0,25 \text{ Liter}")
            st.write("Langkah 3: Jalankan rumus pembagian molaritas:")
            st.latex(r"M = \frac{0,1 \text{ mol}}{0,25 \text{ Liter}} = 0,4 \text{ M}")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Berapa gram kristal garam NaCl (Mr = 58,5) yang harus ditimbang untuk membuat larutan garam dapur konsentrasi 0,2 M dengan volume tepat 500 mL?")

    with tab_kuis:
        st.subheader("✍️ Kuis Akhir Evaluasi Level 2")
        st.write("Uji pemahaman belajarmu dengan menjawab 15 soal pilihan ganda di bawah ini secara mandiri.")
        st.write("---")
        
        # 15 Soal Pilihan Ganda Komprehensif (Bebas Bug Kode HTML)
        q1 = st.radio("1. Massa dari 2 mol molekul air (H₂O, Mr = 18) adalah...", ["18 gram", "36 gram", "9 gram", "54 gram"], key="k2_q1")
        q2 = st.radio("2. Jumlah mol atom Karbon yang terdapat di dalam 12 gram sampel karbon murni (Ar C = 12) adalah...", ["0,5 mol", "1 mol", "2 mol", "12 mol"], key="k2_q2")
        q3 = st.radio("3. Berapakah jumlah atom total yang terdapat di dalam 0,5 mol logam Tembaga (Cu)?", ["3,01 x 10²³ atom", "6,02 x 10²³ atom", "1,204 x 10²⁴ atom", "3,01 x 10²² atom"], key="k2_q3")
        q4 = st.radio("4. Suatu sampel gas mengandung 1,204 x 10²⁴ molekul CO₂. Jumlah mol gas tersebut adalah...", ["0,5 mol", "1 mol", "2 mol", "4 mol"], key="k2_q4")
        q5 = st.radio("5. Jika massa dari 3,01 x 10²³ atom suatu logam murni adalah 28 gram, berapakah Ar logam tersebut?", ["14 g/mol", "28 g/mol", "56 g/mol", "112 g/mol"], key="k2_q5")
        q6 = st.radio("6. Berapakah volume dari 0,25 mol gas oksigen (O₂) jika diukur pada keadaan standar (STP)?", ["2,8 Liter", "5,6 Liter", "11,2 Liter", "22,4 Liter"], key="k2_q6")
        q7 = st.radio("7. Gas metana (CH₄, Mr = 16) bermassa 8 gram jika diukur pada kondisi kamar (RTP) memiliki volume sebesar...", ["5,6 Liter", "11,2 Liter", "12 Liter", "24 Liter"], key="k2_q7")
        q8 = st.radio("8. Hitunglah volume dari 0,5 mol gas ideal yang berada dalam wadah bersuhu 27°C (300 K) bertekanan 1 atm! (R = 0,082)", ["11,2 Liter", "12,3 Liter", "22,4 Liter", "24,6 Liter"], key="k2_q8")
        q9 = st.radio("9. Pada suhu dan tekanan tertentu, 2 mol gas O₂ bervolume 10 Liter. Pada kondisi lingkungan yang sama, volume dari 4 mol gas CO₂ adalah...", ["5 Liter", "10 Liter", "20 Liter", "40 Liter"], key="k2_q9")
        q10 = st.radio("10. Jika 4,48 Liter gas N₂ pada keadaan STP ditimbang, berapakah massa gas tersebut? (Mr N₂ = 28)", ["2,8 gram", "5,6 gram", "7 gram", "14 gram"], key="k2_q10")
        q11 = st.radio("11. Sebanyak 0,1 mol asam klorida (HCl) dilarutkan ke dalam air hingga volume 500 mL. Berapakah molaritas larutan?", ["0,05 M", "0,1 M", "0,2 M", "0,5 M"], key="k2_q11")
        q12 = st.radio("12. Larutan NaOH dengan konsentrasi 0,4 M mengandung zat terlarut sebanyak 0,1 mol. Berapakah volume larutan tersebut?", ["100 mL", "250 mL", "400 mL", "500 mL"], key="k2_q12")
        q13 = st.radio("13. Berapakah jumlah partikel molekul yang ada di dalam 11,2 Liter gas ideal pada kondisi STP?", ["1,505 x 10²³", "3,01 x 10²³", "6,02 x 10²³", "1,204 x 10²⁴"], key="k2_q13")
        q14 = st.radio("14. Massa dari 1 mol gas ideal X₂ pada STP adalah 32 gram. Unsur X yang dimaksud adalah...", ["Hidrogen (Ar=1)", "Karbon (Ar=12)", "Nitrogen (Ar=14)", "Oksigen (Ar=16)"], key="k2_q14")
        q15 = st.radio("15. Larutan garam dapur dibuat dengan melarutkan 5,85 gram NaCl (Mr = 58,5) ke dalam air hingga volume 1 Liter. Konsentrasi larutan tersebut adalah...", ["0,01 M", "0,1 M", "0,5 M", "1,0 M"], key="k2_q15")

        st.write("---")
        if st.button("Periksa Hasil Jawaban & Lihat Pembahasan Level 2 📝"):
            skor_hitung = 0
            if q1 == "36 gram": skor_hitung += 1
            if q2 == "1 mol": skor_hitung += 1
            if q3 == "3,01 x 10²³ atom": skor_hitung += 1
            if q4 == "2 mol": skor_hitung += 1
            if q5 == "56 g/mol": skor_hitung += 1
            if q6 == "5,6 Liter": skor_hitung += 1
            if q7 == "12 Liter": skor_hitung += 1
            if q8 == "12,3 Liter": skor_hitung += 1
            if q9 == "20 Liter": skor_hitung += 1
            if q10 == "5,6 gram": skor_hitung += 1
            if q11 == "0,2 M": skor_hitung += 1
            if q12 == "250 mL": skor_hitung += 1
            if q13 == "3,01 x 10²³": skor_hitung += 1
            if q14 == "Oksigen (Ar=16)": skor_hitung += 1
            if q15 == "0,1 M": skor_hitung += 1
            
            skor_final = round((skor_hitung / 15) * 100)
            st.success(f"Evaluasi selesai! Kamu menjawab {skor_hitung} dari 15 soal dengan benar. Skor kamu: {skor_final} / 100.")
            st.balloons()
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Detil Atas-Bawah:")
            
            st.markdown("**Soal 1**")
            st.latex(r"\text{Massa} = n \times Mr = 2 \text{ mol} \times 18 \text{ g/mol} = 36 \text{ gram}")
            
            st.markdown("**Soal 2**")
            st.latex(r"n = \frac{\text{Massa}}{Ar} = \frac{12 \text{ gram}}{12 \text{ g/mol}} = 1 \text{ mol}")
            
            st.markdown("**Soal 3**")
            st.latex(r"X = n \times 6,02 \times 10^{23} = 0,5 \times 6,02 \times 10^{23} = 3,01 \times 10^{23} \text{ atom}")
            
            st.markdown("**Soal 4**")
            st.latex(r"n = \frac{1,204 \times 10^{24}}{6,02 \times 10^{23}} = 2 \text{ mol}")
            
            st.markdown("**Soal 5**")
            st.write("Cari jumlah mol (n) molekul terlebih dahulu:")
            st.latex(r"n = \frac{3,01 \times 10^{23}}{6,02 \times 10^{23}} = 0,5 \text{ mol}")
            st.write("Kemudian hitung Massa Atom Relatif (Ar):")
            st.latex(r"Ar = \frac{\text{Massa}}{n} = \frac{28 \text{ gram}}{0,5 \text{ mol}} = 56 \text{ g/mol}")
            
            st.markdown("**Soal 6**")
            st.latex(r"V_{\text{STP}} = n \times 22,4 = 0,25 \times 22,4 = 5,6 \text{ Liter}")
            
            st.markdown("**Soal 7**")
            st.write("Cari jumlah mol (n):")
            st.latex(r"n = \frac{8 \text{ gram}}{16 \text{ g/mol}} = 0,5 \text{ mol}")
            st.write("Maka volume keadaan kamar (RTP):")
            st.latex(r"V_{\text{RTP}} = n \times 24 = 0,5 \times 24 = 12 \text{ Liter}")
            
            st.markdown("**Soal 8**")
            st.latex(r"V = \frac{n \times R \times T}{P} = \frac{0,5 \times 0,082 \times 300}{1} = 12,3 \text{ Liter}")
            
            st.markdown("**Soal 9**")
            st.write("Perbandingan volume gas sebanding dengan perbandingan jumlah molnya:")
            st.latex(r"V_2 = \frac{n_2}{n_1} \times V_1 = \frac{4 \text{ mol}}{2 \text{ mol}} \times 10 \text{ L} = 20 \text{ Liter}")
            
            st.markdown("**Soal 10**")
            st.write("Cari jumlah mol (n):")
            st.latex(r"n = \frac{4,48 \text{ L}}{22,4 \text{ L/mol}} = 0,2 \text{ mol}")
            st.write("Massa komponen gas:")
            st.latex(r"\text{Massa} = 0,2 \text{ mol} \times 28 \text{ g/mol} = 5,6 \text{ gram}")
            
            st.markdown("**Soal 11**")
            st.latex(r"M = \frac{n}{V} = \frac{0,1 \text{ mol}}{0,5 \text{ Liter}} = 0,2 \text{ M}")
            
            st.markdown("**Soal 12**")
            st.latex(r"V = \frac{n}{M} = \frac{0,1 \text{ mol}}{0,4 \text{ M}} = 0,25 \text{ Liter} = 250 \text{ mL}")
            
            st.markdown("**Soal 13**")
            st.write("Cari jumlah mol (n) gas:")
            st.latex(r"n = \frac{11,2 \text{ L}}{22,4 \text{ L/mol}} = 0,5 \text{ mol}")
            st.write("Hitung kuantitas partikel (X):")
            st.latex(r"X = 0,5 \times 6,02 \times 10^{23} = 3,01 \times 10^{23} \text{ molekul}")
            
            st.markdown("**Soal 14**")
            st.write("Karena 1 mol gas bermassa 32 gram, maka Mr X₂ = 32. Sehingga nilai Ar X = 16 (Unsur Oksigen).")
            
            st.markdown("**Soal 15**")
            st.write("Cari jumlah mol (n):")
            st.latex(r"n = \frac{5,85 \text{ gram}}{58,5 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Hitung konsentrasi akhir Molaritas:")
            st.latex(r"M = \frac{0,1 \text{ mol}}{1 \text{ Liter}} = 0,1 \text{ M}")
elif st.session_state.get('menu_aktif') == 'level_3':
    # --- TOMBOL KEMBALI KE DASHBOARD ---
    if st.button("⬅️ Kembali ke Dashboard"):
        st.session_state.menu_aktif = 'dashboard'
        st.rerun()
        
    st.title("🔥 Level 3: Stoikiometri Persamaan Reaksi & Tabel M-R-S")
    
    tab_materi, tab_kuis = st.tabs(["📖 Materi Pembelajaran", "✍️ Kuis Evaluasi Level 3"])

    with tab_materi:
        # --- Bagian A: Makna Koefisien Reaksi ---
        st.header("A. Makna Koefisien Reaksi & Perbandingan Mol")
        st.write("Pada Level 1 dan 2, kita telah mempelajari cara menyetarakan reaksi dan mengubah satuan zat menjadi mol. Sekarang, kita akan menggabungkan keduanya.")
        st.write("Prinsip utama dalam perhitungan persamaan reaksi kimia adalah: **Perbandingan koefisien reaksi murni menyatakan perbandingan jumlah mol zat-zat yang terlibat dalam reaksi** (baik reaktan maupun produk).")
        
        st.write("Secara matematis, jika kita ingin mencari mol suatu zat dari zat lain yang sudah diketahui, kita gunakan rumus pecahan pembilang-penyebut berikut:")
        st.latex(r"\text{Mol Zat Ditanya} = \frac{\text{Koefisien Zat Ditanya}}{\text{Koefisien Zat Diketahui}} \times \text{Mol Zat Diketahui}")

        st.markdown("**📝 Contoh Soal dengan Pembahasan:**")
        st.write("Gas hidrogen dibakar dengan gas oksigen menghasilkan uap air melalui persamaan reaksi yang telah setara berikut:")
        st.info("**2 H₂ + O₂  →  2 H₂O**")
        st.write("Jika gas hidrogen (H₂) yang bereaksi adalah sebanyak 0,6 mol, berapakah jumlah mol gas oksigen (O₂) yang dibutuhkan?")
        
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Gunakan rumus perbandingan koefisien atas-bawah murni:")
            st.latex(r"n_{\text{O}_2} = \frac{\text{Koefisien O}_2}{\text{Koefisien H}_2} \times n_{\text{H}_2}")
            st.latex(r"n_{\text{O}_2} = \frac{1}{2} \times 0,6 \text{ mol} = 0,3 \text{ mol}")
            st.write("Jadi, gas oksigen yang dibutuhkan untuk menghabiskan hidrogen tersebut adalah 0,3 mol.")
            
        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Pada reaksi pembakaran gas propana: **C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O**. Jika di dalam wadah terbentuk tepat 1,2 mol uap air (H₂O), berapakah mol gas CO₂ yang juga ikut terbentuk pada reaksi tersebut?")
        st.write("---")

        # --- Bagian B: Konsep Pereaksi Pembatas ---
        st.header("B. Konsep & Cara Menentukan Pereaksi Pembatas")
        st.write("Dalam eksperimen nyata di laboratorium, jarang sekali kita mencampurkan reaktan dalam perbandingan mol yang tepat pas sesuai koefisien reaksinya. Sering kali, ada zat yang sengaja dibuat berlebih, dan ada zat yang jumlahnya terbatas.")
        st.write("Zat pereaksi yang **habis terlebih dahulu** di dalam suatu reaksi kimia disebut sebagai **Pereaksi Pembatas (Limiting Reactant)**. Zat ini sangat krusial karena ia membatasi atau menentukan jumlah maksimal produk yang dapat terbentuk.")
        
        st.markdown("**💡 Aturan Emas Mencari Pereaksi Pembatas:**")
        st.write("Jika di dalam soal diketahui jumlah awal (massa/mol/volume) dari **kedua reaktan**, kamu wajib melakukan uji pembagian nilai pembilang-penyebut berikut:")
        st.latex(r"\text{Nilai Uji Pembatas} = \frac{\text{Jumlah Mol Mula-mula}}{\text{Koefisien Reaksi Zat Tersebut}}")
        st.write("Bandingkan hasil bagi dari semua reaktan. Zat yang memiliki **Nilai Uji Pembatas paling kecil** ditetapkan sebagai **Pereaksi Pembatas**.")

        st.markdown("**📝 Contoh Soal dengan Pembahasan:**")
        st.write("Logam Aluminium dilarutkan ke dalam larutan asam sulfat dengan persamaan reaksi:")
        st.info("**2 Al + 3 H₂SO₄  →  Al₂(SO₄)₃ + 3 H₂**")
        st.write("Jika di awal reaksi dicampurkan 0,6 mol logam Al dan 0,6 mol larutan H₂SO₄, tentukan zat manakah yang bertindak sebagai pereaksi pembatas!")
        
        with st.expander("Klik untuk Lihat Pembahasan"):
            st.write("Lakukan uji pembatas dengan membagi mol awal terhadap koefisien masing-masing reaktan:")
            st.write("1. Nilai uji untuk logam Al:")
            st.latex(r"\text{Uji Al} = \frac{0,6 \text{ mol}}{2} = 0,3")
            st.write("2. Nilai uji untuk larutan H₂SO₄:")
            st.latex(r"\text{Uji H}_2\text{SO}_4 = \frac{0,6 \text{ mol}}{3} = 0,2")
            st.write("Sekarang bandingkan hasil ujinya: karena **0,2 (H₂SO₄) < 0,3 (Al)**, maka zat yang bertindak sebagai pereaksi pembatas adalah **H₂SO₄**. Zat H₂SO₄ inilah yang akan habis tak bersisa dan menjadi patokan hitungan selanjutnya.")

        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Gas metana dibakar dengan gas oksigen: **CH₄ + 2 O₂ → CO₂ + 2 H₂O**. Jika mula-mula dicampurkan 1,5 mol CH₄ dan 2 mol O₂, tentukan zat reaktan manakah yang akan habis bereaksi terlebih dahulu!")
        st.write("---")

        # --- Bagian C: Tabel M-R-S ---
        st.header("C. Integrasi Perhitungan dengan Tabel M-R-S")
        st.write("Setelah kamu bisa menentukan siapa pereaksi pembatas yang menjadi otak kendali reaksi, sekarang kita gunakan alat bantu visual bernama **Tabel M-R-S (Mula-mula, Reaksi, Sisa)** untuk mencatat aliran perubahan zat.")
        
        st.markdown("""
        * **(M) Mula-mula:** Mengisi mol awal zat sebelum bereaksi. Zat produk di sebelah kanan tanda panah selalu bernilai nol (atau strip `-`) karena belum terbentuk.
        * **(R) Reaksi:** Mengisi mol zat yang terlibat perubahan. **Baris ini wajib berpatokan pada perbandingan koefisien dikali mol milik Pereaksi Pembatas.** Reaktan diberi tanda minus (berkurang) dan produk diberi tanda plus (bertambah).
        * **(S) Sisa:** Keadaan akhir setelah reaksi berhenti.
          * Sisa Reaktan (Kiri) = Mula-mula $-$ Reaksi.
          * Sisa Produk (Kanan) = Mula-mula $+$ Reaksi.
        """)

        st.markdown("**📝 Contoh Soal Komprehensif dengan Pembahasan:**")
        st.write("Sebanyak 5,6 gram logam besi (Fe, Ar = 56) direaksikan dengan larutan yang mengandung 0,3 mol asam klorida (HCl) menurut reaksi:")
        st.info("**Fe + 2 HCl  →  FeCl₂ + H₂**")
        st.write("Hitunglah berapakah volume gas hidrogen (H₂) yang dihasilkan jika diukur pada keadaan standar (STP)!")
        
        with st.expander("Klik untuk Lihat Langkah Penyelesaian M-R-S"):
            st.write("**Langkah 1: Cari mol awal semua komponen reaktan**")
            st.latex(r"n_{\text{Fe}} \text{ mula-mula} = \frac{5,6 \text{ gram}}{56 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Mol HCl mula-mula sudah diketahui dari soal = 0,3 mol.")
            
            st.write("**Langkah 2: Tentukan Pereaksi Pembatas**")
            st.latex(r"\text{Uji Fe} = \frac{0,1}{1} = 0,1 \quad | \quad \text{Uji HCl} = \frac{0,3}{2} = 0,15")
            st.write("Karena hasil uji Fe (0,1) lebih kecil dari HCl (0,15), maka **Fe adalah Pereaksi Pembatas (Habis)**.")
            
            st.write("**Langkah 3: Susun Jalannya Tabel M-R-S**")
            st.write("Karena Fe habis, maka di baris Reaksi, Fe berkurang sebesar 0,1 mol. Gunakan perbandingan koefisien untuk mengisi komponen zat lainnya:")
            st.latex(r"n_{\text{HCl}} \text{ bereaksi} = \frac{2}{1} \times 0,1 \text{ mol} = 0,2 \text{ mol}")
            st.latex(r"n_{\text{H}_2} \text{ terbentuk} = \frac{1}{1} \times 0,1 \text{ mol} = 0,1 \text{ mol}")
            
            st.markdown("""
            | Komponen Tabel | Fe | + 2 HCl | → FeCl₂ | + H₂ |
            | :--- | :---: | :---: | :---: | :---: |
            | **Mula-mula (M)** | 0,1 mol | 0,3 mol | - | - |
            | **Reaksi (R)** | -0,1 mol | -0,2 mol | +0,1 mol | +0,1 mol |
            | **Sisa (S)** | 0 mol | 0,1 mol | 0,1 mol | 0,1 mol |
            """)
            
            st.write("**Langkah 4: Konversikan nilai sisa produk ke satuan tujuan**")
            st.write("Berdasarkan tabel baris sisa, gas H₂ yang diperoleh berwujud 0,1 mol. Kita ubah ke Volume STP:")
            st.latex(r"V_{\text{STP}} = n_{\text{H}_2} \times 22,4 \text{ L/mol} = 0,1 \text{ mol} \times 22,4 \text{ L/mol} = 2,24 \text{ Liter}")

        st.markdown("**✍️ Latihan Mandiri (Tanpa Pembahasan):**")
        st.info("Sebanyak 2 mol gas belerang dioksida direaksikan dengan 2 mol gas oksigen menurut persamaan: **2 SO₂ + O₂ → 2 SO₃**. Buatlah analisis coretan tabel M-R-S di buku tugasmu, lalu tentukan berapakah jumlah mol senyawa SO₃ yang berhasil terbentuk di akhir reaksi!")

    with tab_kuis:
        st.subheader("✍️ Kuis Evaluasi Komprehensif Level 3")
        st.write("Uji pemahaman analisismu mengenai Koefisien, Pereaksi Pembatas, dan Tabel M-R-S melalui 10 soal pilihan ganda di bawah ini.")
        st.write("---")
        
        q1 = st.radio("1. Diketahui reaksi: N₂ + 3 H₂ → 2 NH₃. Jika direaksikan 2 mol gas N₂ dengan H₂ berlebih, berapakah mol gas NH₃ yang dihasilkan?", ["2 mol", "3 mol", "4 mol", "6 mol"], key="k3_q1")
        q2 = st.radio("2. Reaksi pembentukan air: 2 H₂ + O₂ → 2 H₂O. Untuk menghasilkan tepat 36 gram H₂O (Mr = 18), berapakah massa gas hidrogen (H₂, Mr = 2) yang bereaksi?", ["2 gram", "4 gram", "8 gram", "16 gram"], key="k3_q2")
        q3 = st.radio("3. Sebanyak 2,4 gram pita Magnesium (Ar Mg = 24) dimasukkan ke dalam larutan HCl berlebih (Mg + 2 HCl → MgCl₂ + H₂). Berapa volume gas H₂ yang terbentuk pada keadaan kamar (RTP)?", ["1,2 Liter", "2,4 Liter", "11,2 Liter", "22,4 Liter"], key="k3_q3")
        q4 = st.radio("4. Pada reaksi: A + 2 B → AB₂. Jika dicampurkan 2 mol zat A dan 3 mol zat B, zat manakah yang bertindak sebagai pereaksi pembatas?", ["Zat A", "Zat B", "Senyawa AB₂", "Keduanya habis"], key="k3_q4")
        q5 = st.radio("5. Belerang dibakar menurut reaksi: S + O₂ → SO₂. Jika disediakan 32 gram S (Ar = 32) dan 32 gram O₂ (Mr = 32), berapakah massa gas SO₂ (Mr = 64) yang dihasilkan di akhir reaksi?", ["32 gram", "48 gram", "64 gram", "128 gram"], key="k3_q5")
        q6 = st.radio("6. Sebanyak 0,2 mol besi (Fe) dimasukkan ke dalam gelas yang berisi 0,2 mol HCl (Fe + 2 HCl → FeCl₂ + H₂). Setelah reaksi selesai, zat apakah yang BERSISA?", ["Besi (Fe)", "Asam klorida (HCl)", "Keduanya habis", "Gas H₂"], key="k3_q6")
        q7 = st.radio("7. Melanjutkan soal nomor 6 di atas, berapakah mol gas H₂ yang terbentuk di akhir reaksi?", ["0,1 mol", "0,2 mol", "0,3 mol", "0,4 mol"], key="k3_q7")
        q8 = st.radio("8. Direaksikan larutan yang mengandung 0,02 mol NaOH dengan larutan yang mengandung 0,02 mol HCl (NaOH + HCl → NaCl + H₂O). Berapa massa garam NaCl (Mr = 58,5) yang diperoleh?", ["0,585 gram", "1,17 gram", "5,85 gram", "11,7 gram"], key="k3_q8")
        q9 = st.radio("9. Logam Aluminium bereaksi: 2 Al + 3 H₂SO₄ → Al₂(SO₄)₃ + 3 H₂. Jika direaksikan 0,2 mol Al dengan 0,6 mol H₂SO₄, siapakah pereaksi pembatasnya?", ["Aluminium (Al)", "Asam Sulfat (H₂SO₄)", "Keduanya habis", "Gas H₂"], key="k3_q9")
        q10 = st.radio("10. Reaksi pembakaran metana: CH₄ + 2 O₂ → CO₂ + 2 H₂O. Jika mula-mula direaksikan 2 mol CH₄ dan 3 mol O₂, pada tabel akhir reaksi (Sisa), berapa mol gas CO₂ yang terbentuk dan berapa mol reaktan yang bersisa?", ["1 mol CO₂, sisa 0,5 mol CH₄", "1,5 mol CO₂, sisa 0,5 mol CH₄", "2 mol CO₂, sisa 1 mol O₂", "1,5 mol CO₂, sisa 1 mol O₂"], key="k3_q10")

        st.write("---")
        if st.button("Periksa Hasil Jawaban & Lihat Pembahasan M-R-S 📝"):
            skor_hitung = 0
            if q1 == "4 mol": skor_hitung += 1
            if q2 == "4 gram": skor_hitung += 1
            if q3 == "2,4 Liter": skor_hitung += 1
            if q4 == "Zat B": skor_hitung += 1
            if q5 == "64 gram": skor_hitung += 1
            if q6 == "Besi (Fe)": skor_hitung += 1
            if q7 == "0,1 mol": skor_hitung += 1
            if q8 == "1,17 gram": skor_hitung += 1
            if q9 == "Aluminium (Al)": skor_hitung += 1
            if q10 == "1,5 mol CO₂, sisa 0,5 mol CH₄": skor_hitung += 1
            
            skor_final = round((skor_hitung / 10) * 100)
            st.success(f"Evaluasi selesai! Kamu menjawab {skor_hitung} dari 10 soal dengan benar. Skor kamu: {skor_final} / 100.")
            st.balloons()
            
            st.markdown("### 💡 Kunci Jawaban & Pembahasan Detil Tabel M-R-S:")
            
            st.markdown("**Soal 1**")
            st.write("Karena H₂ berlebih, N₂ otomatis bertindak sebagai pereaksi pembatas. Rumus mencari produk amonia:")
            st.latex(r"n_{\text{NH}_3} = \frac{2}{1} \times 2 \text{ mol} = 4 \text{ mol}")
            
            st.markdown("**Soal 2**")
            st.write("Langkah 1: Cari mol produk H₂O:")
            st.latex(r"n_{\text{H}_2\text{O}} = \frac{36 \text{ gram}}{18 \text{ g/mol}} = 2 \text{ mol}")
            st.write("Langkah 2: Cari mol H₂ di baris Reaksi berdasarkan perbandingan koefisien:")
            st.latex(r"n_{\text{H}_2} = \frac{2}{2} \times 2 \text{ mol} = 2 \text{ mol}")
            st.write("Langkah 3: Ubah mol H₂ menjadi gram:")
            st.latex(r"\text{Massa H}_2 = 2 \text{ mol} \times 2 \text{ g/mol} = 4 \text{ gram}")
            
            st.markdown("**Soal 3**")
            st.write("Langkah 1: Ubah Mg ke mol:")
            st.latex(r"n_{\text{Mg}} = \frac{2,4 \text{ gram}}{24 \text{ g/mol}} = 0,1 \text{ mol}")
            st.write("Langkah 2: Karena koefisien Mg dan H₂ sama (1:1), maka mol H₂ = 0,1 mol.")
            st.write("Langkah 3: Hitung volume keadaan kamar (RTP):")
            st.latex(r"V_{\text{RTP}} = 0,1 \text{ mol} \times 24 \text{ L/mol} = 2,4 \text{ Liter}")
            
            st.markdown("**Soal 4**")
            st.write("Uji nilai pembatas:")
            st.latex(r"\text{Uji A} = \frac{2 \text{ mol}}{1} = 2 \quad | \quad \text{Uji B} = \frac{3 \text{ mol}}{2} = 1,5")
            st.write("Karena nilai uji B lebih kecil, maka **Zat B adalah Pereaksi Pembatas**.")
            
            st.markdown("**Soal 5**")
            st.write("Mol S = 1 mol dan Mol O₂ = 1 mol. Karena rasio koefisiennya 1:1, kedua reaktan habis bersamaan tanpa sisa. Terbentuk produk SO₂ sebanyak 1 mol.")
            st.latex(r"\text{Massa SO}_2 = 1 \text{ mol} \times 64 \text{ g/mol} = 64 \text{ gram}")
            
            st.markdown("**Soal 6**")
            st.write("Lakukan uji pembatas reaktan:")
            st.latex(r"\text{Uji Fe} = \frac{0,2}{1} = 0,2 \quad | \quad \text{Uji HCl} = \frac{0,2}{2} = 0,1")
            st.write("Sesuai aturan emas, karena uji HCl lebih kecil, maka HCl habis. Fe bertindak sebagai zat yang bersisa:")
            st.latex(r"n_{\text{Fe}} \text{ bereaksi} = \frac{1}{2} \times 0,2 \text{ mol} = 0,1 \text{ mol}")
            st.write("Sisa Fe di baris akhir tabel = 0,2 mol (mula-mula) - 0,1 mol (reaksi) = 0,1 mol. Maka **Besi (Fe) bersisa**.")
            
            st.markdown("**Soal 7**")
            st.write("Gunakan data mol pembatas yang habis (HCl = 0,2 mol) sebagai acuan mencari gas H₂:")
            st.latex(r"n_{\text{H}_2} = \frac{1}{2} \times 0,2 \text{ mol} = 0,1 \text{ mol}")
            
            st.markdown("**Soal 8**")
            st.write("Karena mol awal dan koefisien NaOH serta HCl setara 1:1, keduanya habis bereaksi dan menghasilkan tepat 0,02 mol NaCl.")
            st.latex(r"\text{Massa NaCl} = 0,02 \text{ mol} \times 58,5 \text{ g/mol} = 1,17 \text{ gram}")
            
            st.markdown("**Soal 9**")
            st.write("Uji nilai pembatas pembilang-penyebut:")
            st.latex(r"\text{Uji Al} = \frac{0,2 \text{ mol}}{2} = 0,1 \quad | \quad \text{Uji H}_2\text{SO}_4 = \frac{0,6 \text{ mol}}{3} = 0,2")
            st.write("Karena hasil bagi Al lebih kecil (0,1 < 0,2), maka **Aluminium (Al) adalah pereaksi pembatas**.")
            
            st.markdown("**Soal 10**")
            st.write("Analisis runut Tabel M-R-S:")
            st.write("- Mula-mula: CH₄ = 2 mol, O₂ = 3 mol.")
            st.latex(r"\text{Uji CH}_4 = \frac{2}{1} = 2 \quad | \quad \text{Uji O}_2 = \frac{3}{2} = 1,5")
            st.write("- Reaksi: O₂ habis bereaksi (-3 mol). CH₄ berkurang:")
            st.latex(r"n_{\text{CH}_4} \text{ bereaksi} = \frac{1}{2} \times 3 \text{ mol} = 1,5 \text{ mol}")
            st.write("- Produk CO₂ yang bertambah di baris Reaksi:")
            st.latex(r"n_{\text{CO}_2} \text{ terbentuk} = \frac{1}{2} \times 3 \text{ mol} = 1,5 \text{ mol}")
            st.write("- Keadaan Akhir (Sisa): CH₄ bersisa (2 - 1,5 = 0,5 mol) dan terbentuk 1,5 mol gas CO₂.")
            
# ==================================================
# TOMBOL LOGOUT (Selalu di paling bawah)
# ==================================================
st.write("---")
if st.button("Keluar"):
    st.session_state.sudah_login = False
    st.session_state.username = ""
    if 'menu_aktif' in st.session_state:
        del st.session_state.menu_aktif
    st.rerun()
    
