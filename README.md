# Tugas-Zoom-Practitioner-Lecture

# Studi Kasus 1: Mengurangi Dropout Peserta pada Platform Kursus Online (Berdasarkan Sesi 1: Make Sense of Data with Analysis and AI)

**Latar Belakang Kasus:**

BelajarKu adalah platform kursus online yang memiliki ribuan peserta di kategori Programming, Desain, Bisnis, dan Data Science. Dalam beberapa bulan terakhir, jumlah pendaftar terus naik, namun banyak peserta berhenti di tengah kursus (dropout). Manajemen meminta tim data untuk mencari penyebab masalah ini dan memberikan rekomendasi tindakan.

**Penerapan 4 Level Analisis Data:**

1. **Descriptive Analytics (Apa yang terjadi?)**
   Dari data 997 peserta, tingkat dropout mencapai 25,7%. Kategori Programming memiliki dropout tertinggi (30,0%), sedangkan Desain dan Data Science lebih rendah (sekitar 23%).

2. **Diagnostic Analytics (Mengapa terjadi?)**
   Peserta yang tidak berinteraksi dengan mentor memiliki dropout 36,0%, sedangkan yang berinteraksi hanya 14,6%. Peserta yang login kurang dari 2 kali per minggu memiliki dropout di atas 76%. Jumlah tugas yang banyak dan video yang terlalu panjang juga berkorelasi positif dengan dropout.

3. **Predictive Analytics (Apa yang akan terjadi?)**
   Tim membangun model Random Forest untuk memprediksi peserta yang berpotensi dropout. Model mencapai akurasi 94,5% pada data uji. Faktor paling berpengaruh adalah frekuensi login per minggu, diikuti jumlah tugas dan durasi video.

4. **Prescriptive Analytics (Apa tindakan yang disarankan?)**
   - Mengirim pengingat otomatis kepada peserta yang login kurang dari 2 kali per minggu
   - Menyediakan sesi mentor untuk peserta berisiko tinggi (236 peserta dengan probabilitas dropout di atas 70%)
   - Memecah video berdurasi lebih dari 60 menit menjadi modul pendek
   - Membatasi jumlah tugas per modul maksimal 8

**Peran Manusia dan Generative AI:**

Generative AI digunakan untuk mempercepat pembuatan skrip pembersihan data dan merangkum pola dari data peserta. Namun, verifikasi hasil analisis dan keputusan akhir kebijakan (misalnya program mentoring dan batas tugas) tetap dilakukan oleh manusia.

# Studi Kasus 2: Simulasi Risiko Banjir Kota Menggunakan HPC (Berdasarkan Sesi 2: Bridging Global Infrastructure to Address Local Challenge with HPC)

**Latar Belakang Kasus:**

Pemerintah Kota Tirta Raya memiliki sungai utama yang melintasi kawasan padat penduduk. Setiap musim hujan, sungai ini berisiko meluap dan menggenangi permukiman serta jalan utama. Dinas Penanggulangan Bencana membutuhkan sistem peringatan dini yang mampu menghitung peluang banjir dari jutaan kemungkinan skenario cuaca. Masalahnya, jika simulasi dijalankan di satu komputer biasa, prosesnya memakan waktu terlalu lama sehingga peringatan datang setelah air terlanjur naik.

**Solusi Berbasis HPC (High Performance Computing):**

1. **Pemodelan dan Simulasi Komputasi Skala Besar:**

   Tim memodelkan dua faktor utama penyebab banjir, yaitu curah hujan (distribusi gamma) dan tingkat kejenuhan tanah (30% sampai 100%). Dari keduanya dihitung debit sungai, lalu dibandingkan dengan kapasitas sungai sebesar 220 m3/detik. Dengan metode Monte Carlo, tim menjalankan 8 juta skenario agar peluang banjir yang dihasilkan stabil dan akurat.

2. **Pemrosesan Paralel dengan MPI:**

   Pekerjaan sebesar itu tidak efisien jika dikerjakan satu prosesor. Dengan MPI, beban dibagi rata ke beberapa proses yang berjalan bersamaan, lalu hasilnya digabung (reduce) di proses utama. Waktu komputasi dibandingkan antara 1 proses dan 4 proses untuk melihat percepatan. Pada HPC sungguhan, prinsip yang sama dijalankan di cluster dengan ratusan sampai ribuan core.
   - Waktu komputasi dengan 1 proses: *(isi hasil komputermu)* detik
   - Waktu komputasi dengan 4 proses: *(isi hasil komputermu)* detik

3. **Integrasi Hasil dan Pengambil Keputusan (The Integrator):**

   Simulasi menghasilkan peluang banjir sekitar 4,6%, yang masuk status AMAN dengan ambang batas 5%. Jika peluang melewati ambang tersebut, status otomatis naik menjadi SIAGA dan sistem merekomendasikan petugas menyiapkan pompa, posko, dan jalur evakuasi.

**Peran Mahasiswa Informatika dan Teknologi HPC:**

HPC berperan sebagai mesin penghitung yang sangat cepat, sehingga jutaan skenario banjir dapat diselesaikan dalam waktu singkat dan hasilnya sempat dimanfaatkan untuk mengambil tindakan. Mahasiswa dan peneliti informatika berperan sebagai penghubung antara infrastruktur komputasi global dan kebutuhan masyarakat lokal, yaitu menjaga kualitas data masukan, menguji kewajaran model, dan menyajikan hasil dalam bentuk status peringatan yang mudah dipahami. Penetapan siaga dan perintah evakuasi tetap menjadi keputusan manusia di Dinas Penanggulangan Bencana, dengan hasil simulasi sebagai bahan pertimbangan.

# Studi Kasus 3: Pemilihan Lokasi Gerai Baru Minimarket Menggunakan GIS (Berdasarkan Sesi 3: Career and Competition in Industrial Era with GIS)

**Latar Belakang Kasus:**

Warung Maju adalah jaringan minimarket yang berencana membuka satu gerai baru di Kota Sinar Pesisir. Manajemen memiliki enam lokasi kandidat, tetapi pemilihan sebelumnya hanya berdasarkan perkiraan dan harga sewa, sehingga beberapa gerai lama sepi pembeli karena berdekatan dengan kompetitor dan jauh dari permukiman. Tim data diminta memakai pendekatan Sistem Informasi Geografis (GIS) agar keputusan lokasi didukung data spasial.

**Penerapan GIS dalam Pengambilan Keputusan:**

**1. Pengumpulan Layer Data Spasial (Data apa yang dibutuhkan?)**

Tim menyiapkan tiga layer data berbasis koordinat, yaitu titik permukiman penduduk (400 titik), lokasi minimarket kompetitor (5 titik), dan enam lokasi kandidat gerai beserta biaya sewanya.

**2. Analisis Spasial (Apa yang diukur?)**

Dua analisis dilakukan untuk setiap kandidat. Pertama, buffer radius 1 km untuk menghitung jumlah rumah yang berada dalam jangkauan gerai. Kedua, pengukuran jarak ke kompetitor terdekat dengan rumus haversine agar jarak dihitung berdasarkan koordinat di permukaan bumi.

**3. Pembobotan dan Skoring (Bagaimana membandingkannya?)**

Setiap kandidat diberi skor dari tiga faktor yang sudah dinormalisasi: jumlah rumah dalam buffer (bobot 50%), jarak ke kompetitor (bobot 30%), dan biaya sewa yang makin murah makin baik (bobot 20%). Bobot ini dapat disesuaikan oleh manajemen sesuai strategi bisnis.

**4. Rekomendasi Keputusan (Lokasi mana yang dipilih?)**

Hasil skoring menempatkan Lokasi 3 di peringkat pertama dengan skor 0,76, karena paling jauh dari kompetitor (2,57 km) meskipun sewanya relatif tinggi. Lokasi 2 dan 4 berada di peringkat berikutnya.

**Peran GIS dan Kompetensi Karier di Era Industri:**

GIS mengubah data lokasi yang tadinya tersebar menjadi informasi yang bisa dibandingkan secara objektif, sehingga perusahaan tidak lagi memilih lokasi hanya berdasarkan intuisi. Bagi lulusan informatika, kemampuan mengolah data spasial menjadi nilai tambah karier di berbagai industri seperti ritel, logistik, dan perencanaan kota. Meski begitu, skor hanya alat bantu. Faktor lain seperti izin usaha, kondisi jalan, dan rencana pengembangan wilayah tetap perlu dinilai manajemen sebelum keputusan akhir diambil.

# Studi Kasus 4: Prediksi Keterlambatan Pengiriman Paket dengan Machine Learning (Berdasarkan Sesi 4: Introduction to Machine Learning)

**Latar Belakang Kasus:**

KilatKirim adalah perusahaan jasa kurir yang melayani ribuan paket setiap hari. Belakangan, keluhan pelanggan soal paket terlambat terus meningkat, tetapi manajemen baru mengetahuinya setelah paket benar-benar terlambat. Tim data diminta membangun sistem berbasis Machine Learning yang dapat memprediksi paket berisiko terlambat sebelum dikirim, sehingga operator bisa mengambil tindakan lebih awal.

**Alur dan Penerapan Metode Machine Learning:**

**1. Pengumpulan dan Pra-pemrosesan Data (Data Preprocessing)**

Tim menggunakan data riwayat pengiriman yang berisi jarak tempuh, berat paket, kondisi hujan, dan pengalaman kurir (dalam bulan). Data duplikat dan nilai kosong dibersihkan, lalu seluruh fitur diseragamkan skalanya dengan standardisasi agar tidak ada fitur yang mendominasi hanya karena satuannya besar.

**2. Unsupervised Learning (Mengelompokkan Pola Pengiriman)**

Metode K-Means membagi pengiriman menjadi 3 klaster tanpa memakai label. Hasilnya, klaster 0 memiliki tingkat keterlambatan tertinggi (54,6%), klaster 1 sedang (30,4%), dan klaster 2 terendah (19,6%). Pengelompokan ini membantu manajemen menemukan jenis pengiriman yang paling rawan terlambat.

**3. Supervised Learning (Klasifikasi Terlambat vs Tepat Waktu)**

Berdasarkan data historis yang sudah berlabel, algoritma Logistic Regression dilatih untuk memprediksi apakah sebuah paket akan terlambat. Data dibagi 80% untuk pelatihan dan 20% untuk pengujian. Dari koefisien model, jarak tempuh dan hujan meningkatkan risiko keterlambatan, sedangkan pengalaman kurir menurunkannya.

**4. Evaluasi Model dan Dampaknya bagi Pelanggan**

Model mencapai akurasi 83,7% pada data uji. Dari confusion matrix, 74 paket terlambat berhasil terdeteksi (TP), 177 paket tepat waktu terbaca benar (TN), 21 paket salah ditandai terlambat (FP), dan 28 paket terlambat terlewat (FN). Nilai FN perlu diperhatikan karena paket terlambat yang tidak terdeteksi tetap merugikan pelanggan.

**Peran Manusia dalam Sistem Prediksi:**

Model hanya memberi peringatan awal, bukan keputusan akhir. Operator tetap menentukan tindakan, misalnya menugaskan kurir yang lebih berpengalaman untuk rute jauh saat hujan atau menginformasikan estimasi baru kepada pelanggan. Data juga perlu dievaluasi berkala, karena pola pengiriman bisa berubah dan model yang dulu akurat bisa menurun kualitasnya.
