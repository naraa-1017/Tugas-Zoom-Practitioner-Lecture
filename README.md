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
