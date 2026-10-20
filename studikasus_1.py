import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


np.random.seed(42)
n = 1000

df = pd.DataFrame({
    "kategori_kursus": np.random.choice(
        ["Programming", "Desain", "Bisnis", "Data Science"], n),
    "durasi_video_menit": np.random.randint(5, 90, n),
    "jumlah_tugas": np.random.randint(0, 12, n),
    "login_per_minggu": np.random.randint(0, 8, n),
    "diskon_persen": np.random.choice([0, 10, 25, 50], n),
    "ada_interaksi_mentor": np.random.choice([0, 1], n),
})


skor_risiko = (
    (df["login_per_minggu"] < 2) * 0.4
    + (df["jumlah_tugas"] > 8) * 0.25
    + (df["ada_interaksi_mentor"] == 0) * 0.2
    + (df["durasi_video_menit"] > 60) * 0.15
    + np.random.rand(n) * 0.2
)
df["dropout"] = (skor_risiko > 0.55).astype(int)


df = df.drop_duplicates().dropna()


print("=" * 60)
print("1. DESCRIPTIVE ANALYTICS - Apa yang terjadi?")
print("=" * 60)
print(f"Total peserta       : {len(df)}")
print(f"Tingkat dropout     : {df['dropout'].mean() * 100:.1f}%")
print("\nDropout per kategori kursus (%):")
print((df.groupby("kategori_kursus")["dropout"].mean() * 100).round(1))


print("\n" + "=" * 60)
print("2. DIAGNOSTIC ANALYTICS - Mengapa terjadi?")
print("=" * 60)
print("Dropout berdasarkan interaksi mentor (0=tidak, 1=ada):")
print((df.groupby("ada_interaksi_mentor")["dropout"].mean() * 100).round(1))
print("\nDropout berdasarkan login per minggu:")
print((df.groupby("login_per_minggu")["dropout"].mean() * 100).round(1))
print("\nKorelasi fitur dengan dropout:")
print(df.drop(columns="kategori_kursus").corr()["dropout"]
      .drop("dropout").sort_values().round(2))


print("\n" + "=" * 60)
print("3. PREDICTIVE ANALYTICS - Siapa yang berpotensi dropout?")
print("=" * 60)
X = pd.get_dummies(df.drop(columns="dropout"), columns=["kategori_kursus"])
y = df["dropout"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print(f"Akurasi model: {accuracy_score(y_test, pred) * 100:.1f}%")
print(classification_report(y_test, pred, target_names=["Lanjut", "Dropout"]))

pentingnya = pd.Series(model.feature_importances_, index=X.columns)
print("Faktor paling berpengaruh:")
print(pentingnya.sort_values(ascending=False).head(4).round(3))


print("\n" + "=" * 60)
print("4. PRESCRIPTIVE ANALYTICS - Rekomendasi tindakan")
print("=" * 60)
df["prob_dropout"] = model.predict_proba(X)[:, 1]
berisiko = df[df["prob_dropout"] > 0.7]
print(f"Peserta berisiko tinggi (probabilitas > 70%): {len(berisiko)} orang")
print("\nRekomendasi:")
print("- Kirim pengingat otomatis ke peserta yang login < 2x per minggu")
print("- Sediakan sesi mentor untuk peserta berisiko tinggi")
print("- Pecah video > 60 menit menjadi modul pendek")
print("- Batasi jumlah tugas per modul maksimal 8")


print("\n" + "=" * 60)
print("PERAN MANUSIA & GENERATIVE AI")
print("=" * 60)
print("AI membantu : membuat skrip pembersihan data & merangkum pola.")
print("Manusia     : memverifikasi hasil dan memutuskan kebijakan akhir.")
