Tugas Practitioner Lecture
Studi Kasus 1: Mengurangi Dropout Peserta pada Platform Kursus Online (Berdasarkan Sesi 1: Make Sense of Data with Analysis and AI)

Latar Belakang Kasus:

BelajarKu adalah platform kursus online yang memiliki ribuan peserta di kategori Programming, Desain, Bisnis, dan Data Science. Dalam beberapa bulan terakhir, jumlah pendaftar terus naik, namun banyak peserta berhenti di tengah kursus (dropout). Manajemen meminta tim data untuk mencari penyebab masalah ini dan memberikan rekomendasi tindakan.

Penerapan 4 Level Analisis Data:

Descriptive Analytics (Apa yang terjadi?) Dari data 997 peserta, tingkat dropout mencapai 25,7%. Kategori Programming memiliki dropout tertinggi (30,0%), sedangkan Desain dan Data Science lebih rendah (sekitar 23%).
Diagnostic Analytics (Mengapa terjadi?) Peserta yang tidak berinteraksi dengan mentor memiliki dropout 36,0%, sedangkan yang berinteraksi hanya 14,6%. Peserta yang login kurang dari 2 kali per minggu memiliki dropout di atas 76%. Jumlah tugas yang banyak dan video yang terlalu panjang juga berkorelasi positif dengan dropout.
Predictive Analytics (Apa yang akan terjadi?) Tim membangun model Random Forest untuk memprediksi peserta yang berpotensi dropout. Model mencapai akurasi 94,5% pada data uji. Faktor paling berpengaruh adalah frekuensi login per minggu, diikuti jumlah tugas dan durasi video.
Prescriptive Analytics (Apa tindakan yang disarankan?)
Mengirim pengingat otomatis kepada peserta yang login kurang dari 2 kali per minggu
Menyediakan sesi mentor untuk peserta berisiko tinggi (236 peserta dengan probabilitas dropout di atas 70%)
Memecah video berdurasi lebih dari 60 menit menjadi modul pendek
Membatasi jumlah tugas per modul maksimal 8

Peran Manusia dan Generative AI:

Generative AI digunakan untuk mempercepat pembuatan skrip pembersihan data dan merangkum pola dari data peserta. Namun, verifikasi hasil analisis dan keputusan akhir kebijakan (misalnya program mentoring dan batas tugas) tetap dilakukan oleh manusia.
