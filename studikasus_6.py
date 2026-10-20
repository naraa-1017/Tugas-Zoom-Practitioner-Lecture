"""
Studi Kasus 6: Klasifikasi Penyebab Kehilangan Hutan Mangrove dengan Citra Satelit dan AI
Berdasarkan Sesi 6: Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

Setiap peringatan (alert) dicirikan oleh data optik (penurunan NDVI) dan radar (perubahan
backscatter), lalu diklasifikasikan penyebabnya. Data sintetis.
Cara menjalankan: python studikasus_6.py   (butuh: pip install pandas numpy scikit-learn)
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import train_test_split

np.random.seed(5)

# Ciri tiap penyebab: (ndvi_turun, radar_db, luas_ha, jarak_jalan_km, ada_api) + jumlah alert
penyebab = {
    "Tambak":           ([0.45, -3.0, 8.0, 2.0, 0.1], 500),
    "Pembukaan jalan":  ([0.30, -1.5, 2.0, 0.3, 0.0], 250),
    "Penebangan":       ([0.25, -2.0, 4.0, 1.5, 0.2], 200),
    "Pertambangan":     ([0.55, -5.0, 12.0, 3.0, 0.0], 50),   # kelas minoritas
}
baris = []
for nama, (mean, jumlah) in penyebab.items():
    data = np.random.normal(mean, [0.1, 1.0, 2.5, 0.8, 0.2], (jumlah, 5))
    kolom = pd.DataFrame(data, columns=["ndvi_turun", "radar_db", "luas_ha", "jarak_jalan_km", "ada_api"])
    kolom["penyebab"] = nama
    baris.append(kolom)
df = pd.concat(baris, ignore_index=True)
df["luas_ha"] = df["luas_ha"].clip(lower=0.2)
df["jarak_jalan_km"] = df["jarak_jalan_km"].clip(lower=0.0)
df["ada_api"] = (df["ada_api"] > 0.5).astype(int)

X, y = df.drop(columns="penyebab"), df["penyebab"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

model = RandomForestClassifier(n_estimators=150, class_weight="balanced", random_state=1)
model.fit(X_tr, y_tr)
pred = model.predict(X_te)

print(f"Overall accuracy : {accuracy_score(y_te, pred) * 100:.1f}%")
print(f"Macro F1-Score   : {f1_score(y_te, pred, average='macro'):.2f}\n")
print(classification_report(y_te, pred))
print("Fitur paling berpengaruh:")
print(pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False).round(2).head(3))
