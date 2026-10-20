"""
Studi Kasus 3: Pemilihan Lokasi Gerai Baru Minimarket Menggunakan GIS
Berdasarkan Sesi 3: Career and Competition in Industrial Era with GIS

Analisis spasial sederhana: buffer radius, jarak ke kompetitor, lalu skoring lokasi.
Data dibuat otomatis (sintetis). Cara menjalankan: python studikasus_3.py
(butuh: pip install pandas numpy)
"""
import numpy as np
import pandas as pd

np.random.seed(7)
PUSAT_LAT, PUSAT_LON = -3.80, 102.26   # titik pusat area studi
RADIUS_KM = 1.0                        # radius buffer (jangkauan gerai)


def acak(n, sebaran=0.03):
    """Bangkitkan n titik koordinat (lat, lon) di sekitar pusat kota."""
    return (PUSAT_LAT + np.random.normal(0, sebaran, n),
            PUSAT_LON + np.random.normal(0, sebaran, n))


def jarak_km(lat1, lon1, lat2, lon2):
    """Jarak antar dua titik (rumus haversine), hasil dalam km."""
    p1, p2 = np.radians(lat1), np.radians(lat2)
    a = (np.sin((p2 - p1) / 2) ** 2
         + np.cos(p1) * np.cos(p2) * np.sin(np.radians(lon2 - lon1) / 2) ** 2)
    return 6371 * 2 * np.arcsin(np.sqrt(a))


# --- Layer data spasial ---
lat_p, lon_p = acak(400)                      # titik permukiman
lat_k, lon_k = acak(5)                        # minimarket kompetitor
lat_c, lon_c = acak(6, 0.025)                 # 6 lokasi kandidat gerai
kandidat = pd.DataFrame({
    "lokasi": [f"Lokasi {c}" for c in "ABCDEF"],
    "sewa_juta": np.random.randint(40, 120, 6),
})

# --- Analisis spasial per kandidat ---
penduduk, jarak_komp = [], []
for i in range(len(kandidat)):
    d_rumah = jarak_km(lat_c[i], lon_c[i], lat_p, lon_p)
    d_komp = jarak_km(lat_c[i], lon_c[i], lat_k, lon_k)
    penduduk.append(int((d_rumah <= RADIUS_KM).sum()))   # buffer 1 km
    jarak_komp.append(round(d_komp.min(), 2))            # kompetitor terdekat
kandidat["rumah_dlm_1km"] = penduduk
kandidat["jarak_kompetitor_km"] = jarak_komp


def norm(x):
    return (x - x.min()) / (x.max() - x.min())


# --- Skoring: makin banyak rumah, makin jauh dari kompetitor, makin murah = makin baik ---
kandidat["skor"] = (0.5 * norm(kandidat["rumah_dlm_1km"])
                    + 0.3 * norm(kandidat["jarak_kompetitor_km"])
                    + 0.2 * (1 - norm(kandidat["sewa_juta"]))).round(2)

hasil = kandidat.sort_values("skor", ascending=False)
print(hasil.to_string(index=False))
print(f"\nRekomendasi lokasi gerai baru: {hasil.iloc[0]['lokasi']}")
