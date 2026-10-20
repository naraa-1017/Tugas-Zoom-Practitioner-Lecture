import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


np.random.seed(11)
n = 1500
df = pd.DataFrame({
    "jarak_km": np.random.uniform(1, 40, n).round(1),
    "berat_kg": np.random.uniform(0.2, 15, n).round(1),
    "hujan": np.random.choice([0, 1], n, p=[0.7, 0.3]),
    "pengalaman_kurir_bln": np.random.randint(1, 48, n),
})
risiko = (0.04 * df["jarak_km"] + 0.5 * df["hujan"]
          + 0.03 * df["berat_kg"] - 0.02 * df["pengalaman_kurir_bln"]
          + np.random.normal(0, 0.3, n))
df["terlambat"] = (risiko > 1.0).astype(int)
df = df.drop_duplicates().dropna()
fitur = ["jarak_km", "berat_kg", "hujan", "pengalaman_kurir_bln"]
X = StandardScaler().fit_transform(df[fitur])


df["klaster"] = KMeans(n_clusters=3, n_init=10, random_state=0).fit_predict(X)
print("Tingkat keterlambatan per klaster (%):")
print((df.groupby("klaster")["terlambat"].mean() * 100).round(1))


X_tr, X_te, y_tr, y_te = train_test_split(
    X, df["terlambat"], test_size=0.2, random_state=0, stratify=df["terlambat"])
model = LogisticRegression().fit(X_tr, y_tr)
pred = model.predict(X_te)


tn, fp, fn, tp = confusion_matrix(y_te, pred).ravel()
print(f"\nAkurasi: {accuracy_score(y_te, pred) * 100:.1f}%")
print(f"Tepat waktu terbaca benar (TN): {tn} | Salah tandai terlambat (FP): {fp}")
print(f"Terlambat terlewat (FN): {fn}      | Terlambat terdeteksi (TP): {tp}")
print("\nPengaruh fitur (koefisien):")
print(pd.Series(model.coef_[0], index=fitur).round(2).sort_values(ascending=False))
