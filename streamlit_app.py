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

        # Dua Tab Utama: Alur Belajar Terstruktur sesuai Keinginanmu
        tab_materi, tab_kuis = st.tabs(["📖 Materi & Latihan Mandiri", "✍️ Kuis Akhir Level 1"])

        # ======================================================================
        # TAB 1: MATERI LENGKAP (5 HUKUM DASAR KIMIA)
        # ======================================================================
        with tab_materi:
            st.write("Selesaikan membaca seluruh materi dan tantangan latihan di bawah ini sebelum maju ke Kuis Akhir!")
            st.write("---")

            # --- 1. LAVOISIER ---
            st.subheader("1. Hukum Kekekalan Massa (Hukum Lavoisier)")
            st.info("Antoine Lavoisier (1789) menemukan bahwa dalam sistem tertutup, **massa total zat sebelum reaksi akan selalu sama dengan massa total zat setelah reaksi.**")
            st.latex(r"\text{S}_{(s)} + \text{Fe}_{(s)} \rightarrow \text{FeS}_{(s)}")
            st.caption("Contoh: 32 gram Belerang + 56 gram Besi = 88 gram Besi(II) Sulfida.")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Sebanyak 10 gram besi ($Fe$) direaksikan dengan 6,4 gram belerang ($S$) menghasilkan senyawa besi(II) sulfida ($FeS$) sepenuhnya. Berapakah massa $FeS$ yang terbentuk?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("**Jawaban:**")
                st.write("Berdasarkan Hukum Kekekalan Massa, massa zat sebelum bereaksi sama dengan massa zat hasil reaksi.")
                st.latex(r"\text{Massa } Fe + \text{Massa } S = \text{Massa } FeS")
                st.latex(r"10\text{ gram} + 6,4\text{ gram} = 16,4\text{ gram}")
                st.write("Jadi, massa $FeS$ yang terbentuk adalah **16,4 gram**.")
                
            st.markdown("##### ✍️ Soal Latihan (Tantangan Mandiri - Tanpa Pembahasan)")
            st.write("Logam magnesium bermassa 4 gram dibakar habis di dalam wadah tertutup dengan gas oksigen. Jika magnesium oksida ($MgO$) yang dihasilkan bermassa 6,6 gram, berapakah massa gas oksigen yang ikut bereaksi?")
            
            st.write("---")

            # --- 2. PROUST ---
            st.subheader("2. Hukum Perbandingan Tetap (Hukum Proust)")
            st.info("Joseph Proust (1799) menyatakan bahwa **perbandingan massa unsur-unsur dalam suatu senyawa adalah selalu tetap dan tertentu.**")
            st.write("Contoh senyawa air ($H_2O$), perbandingan massa Hidrogen ($H$) terhadap Oksigen ($O$) selalu **1 : 8**.")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Perbandingan massa tembaga ($Cu$) dan belerang ($S$) dalam senyawa tembaga(II) sulfida ($CuS$) adalah 2 : 1. Jika direaksikan 10 gram tembaga dengan 3 gram belerang, berapakah massa $CuS$ yang terbentuk?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("**Jawaban:**")
                st.write("Perbandingan $Cu : S = 2 : 1$.")
                st.write("- Jika seluruh $Cu$ habis (10g), maka butuh $S = 1/2 \times 10 = 5\text{ gram}$ (Sulphur tidak cukup karena hanya ada 3g).")
                st.write("- Maka, $S$ yang habis (3g). $Cu$ yang bereaksi $= 2 \times 3 = 6\text{ gram}$.")
                st.latex(r"\text{Massa } CuS = 6\text{g } (Cu) + 3\text{g } (S) = 9\text{ gram}")
                st.write("Zat sisa: Tembaga berlebih sebanyak $10 - 6 = 4\text{ gram}$.")

            st.markdown("##### ✍️ Soal Latihan (Tantangan Mandiri - Tanpa Pembahasan)")
            st.write("Perbandingan massa karbon ($C$) dan oksigen ($O$) dalam karbon dioksida ($CO_2$) adalah 3 : 8. Jika tersedia 12 gram karbon dan 40 gram oksigen, tentukan massa $CO_2$ maksimum yang dapat terbentuk!")

            st.write("---")

            # --- 3. DALTON ---
            st.subheader("3. Hukum Perbandingan Berganda (Hukum Dalton)")
            st.info("John Dalton (1803) menyatakan jika dua unsur membentuk lebih dari satu senyawa, dan jika **massa salah satu unsur dibuat sama**, maka **perbandingan massa unsur lainnya dalam senyawa tersebut merupakan bilangan bulat dan sederhana.**")
            
            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Unsur X dan Y membentuk dua senyawa. Senyawa I mengandung 40% unsur X, dan Senyawa II mengandung 50% unsur X. Buktikan apakah fenomena ini memenuhi Hukum Dalton!")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("**Jawaban:**")
                st.write("- Senyawa I: X = 40%, maka Y = 60%. Perbandingan X : Y = 1 : 1,5")
                st.write("- Senyawa II: X = 50%, maka Y = 50%. Perbandingan X : Y = 1 : 1")
                st.write("Jika massa X dibuat sama (sama-sama bernilai 1), maka perbandingan massa Y pada Senyawa I : Senyawa II = 1,5 : 1 = **3 : 2**.")
                st.write("Karena hasilnya 3 : 2 (bilangan bulat dan sederhana), maka Hukum Dalton **Terbukti**.")

            st.markdown("##### ✍️ Soal Latihan (Tantangan Mandiri - Tanpa Pembahasan)")
            st.write("Nitrogen dan oksigen membentuk senyawa $NO$ dan $NO_2$. Pada senyawa $NO$, persentase massa nitrogen adalah 46,7%. Tunjukkan perbandingan massa oksigen jika massa nitrogen di kedua senyawa tersebut dibuat sama!")

            st.write("---")

            # --- 4. GAY-LUSSAC ---
            st.subheader("4. Hukum Perbandingan Volume (Hukum Gay-Lussac)")
            st.info("Joseph Gay-Lussac (1808) menyatakan bahwa pada suhu dan tekanan yang sama, **volume gas-gas yang bereaksi dan volume gas hasil reaksi berbanding sebagai bilangan bulat dan sederhana.**")
            st.latex(r"\text{N}_{2(g)} + 3\text{H}_{2(g)} \rightarrow 2\text{NH}_{3(g)}")
            st.caption("Perbandingan Volume Gas = 1 : 3 : 2 (searah dengan koefisien reaksinya).")

            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Gas hidrogen sebanyak 6 Liter direaksikan dengan gas oksigen secukupnya untuk membentuk uap air sesuai reaksi: $2\text{H}_{2(g)} + \text{O}_{2(g)} \rightarrow 2\text{H}_2\text{O}_{(g)}$. Berapakah volume uap air yang dihasilkan?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("**Jawaban:**")
                st.write("Berdasarkan Hukum Gay-Lussac, perbandingan volume sama dengan perbandingan koefisien gas.")
                st.write("Perbandingan koefisien $H_2 : H_2O = 2 : 2 = 1 : 1$.")
                st.write("Maka, Volume $H_2O = \frac{2}{2} \times 6\text{ Liter} = 6\text{ Liter}$.")

            st.markdown("##### ✍️ Soal Latihan (Tantangan Mandiri - Tanpa Pembahasan)")
            st.write("Untuk membakar habis 5 Liter gas etana ($C_2H_6$), diperlukan gas oksigen sesuai persamaan reaksi: $2\text{C}_2\text{H}_{6(g)} + 7\text{O}_{2(g)} \rightarrow 4\text{CO}_{2(g)} + 6\text{H}_2\text{O}_{(g)}$. Hitunglah volume gas $CO_2$ yang terbentuk!")

            st.write("---")

            # --- 5. AVOGADRO ---
            st.subheader("5. Hipotesis Avogadro")
            st.info("Amadeo Avogadro (1811) menyatakan bahwa pada suhu dan tekanan yang sama, **semua gas yang volumenya sama akan mengandung jumlah molekul yang sama pula.**")
            st.latex(r"\frac{\text{Volume}_1}{\text{Volume}_2} = \frac{\text{Jumlah Molekul}_1}{\text{Jumlah Molekul}_2} = \frac{\text{Koefisien}_1}{\text{Koefisien}_2}")

            st.markdown("##### 📝 Latihan Soal + Pembahasan")
            st.write("Pada suhu dan tekanan tertentu, 1 Liter gas $N_2$ mengandung $3 \times 10^{22}$ molekul. Pada kondisi yang sama, berapakah jumlah molekul yang terdapat dalam 3 Liter gas $O_2$?")
            with st.expander("Klik di sini untuk melihat Pembahasan"):
                st.write("**Jawaban:**")
                st.write("Gunakan rumus Avogadro:")
                st.latex(r"\frac{V_{N_2}}{V_{O_2}} = \frac{N_{N_2}}{N_{O_2}} \rightarrow \frac{1}{3} = \frac{3 \times 10^{22}}{\text{Jumlah Molekul } O_2}")
                st.write("Jumlah molekul $O_2 = 3 \times (3 \times 10^{22}) = 9 \times 10^{22}\text{ molekul}$.")

            st.markdown("##### ✍️ Soal Latihan (Tantangan Mandiri - Tanpa Pembahasan)")
            st.write("Jika gas hidrogen memiliki koefisien reaksi 2 dan mengandung sebanyak $4 \times 10^{23}$ molekul, hitunglah jumlah molekul gas amonia ($NH_3$) yang koefisien reaksinya adalah 2 pada kondisi suhu dan tekanan yang sama!")


        # ======================================================================
        # TAB 2: KUIS EVALUASI TOTAL (MENGUJI SEMUA HUKUM)
        # ======================================================================
        with tab_kuis:
            st.subheader("✍️ Kuis Evaluasi Komprehensif Level 1")
            st.write("Jawablah 5 soal evaluasi di bawah ini untuk menguji pemahaman totalmu. Syarat lulus minimal benar 4 soal (Skor 80).")
            st.write("---")
            
            q1 = st.radio("Soal 1 (Lavoisier): Sebanyak 7 gram besi direaksikan dengan 4 gram belerang dalam wadah tertutup rapat. Massa besi(II) sulfida yang dihasilkan adalah...", ["7 gram", "4 gram", "11 gram", "28 gram"], key="k1")
            st.write("---")
            q2 = st.radio("Soal 2 (Proust): Perbandingan massa C : O dalam CO2 adalah 3 : 8. Jika direaksikan 6 gram karbon dengan 20 gram oksigen, massa CO2 maksimum yang terbentuk adalah...", ["14 gram", "22 gram", "26 gram", "16 gram"], key="k2")
            st.write("---")
            q3 = st.radio("Soal 3 (Dalton): Dua senyawa nitrogen oksida memiliki perbandingan massa oksigen sebesar 1 : 2 ketika massa nitrogen dibuat sama besar. Fenomena ini mematuhi hukum...", ["Hukum Lavoisier", "Hukum Proust", "Hukum Dalton", "Hipotesis Avogadro"], key="k3")
            st.write("---")
            q4 = st.radio("Soal 4 (Gay-Lussac): Pada reaksi gas N2 + 3H2 -> 2NH3, jika volume gas N2 yang bereaksi adalah 2 Liter, berapakah volume gas H2 yang dibutuhkan?", ["2 Liter", "4 Liter", "6 Liter", "8 Liter"], key="k4")
            st.write("---")
            q5 = st.radio("Soal 5 (Avogadro): Perbandingan volume gas-gas pada kondisi suhu dan tekanan yang sama akan selalu sebanding dengan perbandingan...", ["Massa total zat", "Wujud fisik zat", "Jumlah molekul atau koefisien", "Rumus empiris"], key="k5")
            
            st.write("---")
            if st.button("Kirim Lembar Jawaban Kuis 📝"):
                skor = 0
                if q1 == "11 gram": skor += 20
                if q2 == "22 gram": skor += 20
                if q3 == "Hukum Dalton": skor += 20
                if q4 == "6 Liter": skor += 20
                if q5 == "Jumlah molekul/koefisien": skor += 20
                
                if skor >= 80:
                    st.session_state.level_2_terbuka = True
                    st.balloons()
                    st.success(f"🎉 Luar biasa, Mustofa! Kamu lulus dengan nilai {skor}/100. Kunci Level 2 sekarang resmi TERBUKA!")
                else:
                    st.error(f"❌ Skor kamu: {skor}/100. Syarat KKM adalah 80 (Minimal benar 4 soal). Yuk baca kembali tab materi di atas dan coba lagi!")
                    
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
        
