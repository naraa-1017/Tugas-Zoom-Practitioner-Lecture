import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

poli = ["Umum", "Gigi", "KIA", "Lansia", "Gizi", "Laboratorium"]
tunggu = [48, 22, 35, 61, 18, 40]      # rata-rata waktu tunggu (menit)
TARGET = 30                            # target waktu tunggu maksimal (menit)

fig, (kiri, kanan) = plt.subplots(1, 2, figsize=(12, 5))


kiri.pie(tunggu, labels=poli, autopct="%1.0f%%",
         colors=["red", "blue", "green", "orange", "purple", "cyan"])
kiri.set_title("SEBELUM: sulit dibandingkan")


urut = sorted(zip(tunggu, poli))
nilai, nama = [u[0] for u in urut], [u[1] for u in urut]
warna = ["#d62728" if v > TARGET else "#b0b0b0" for v in nilai]   # pre-attentive: merah = masalah
kanan.barh(nama, nilai, color=warna)
kanan.axvline(TARGET, color="black", linestyle="--")
kanan.text(TARGET + 1, -0.45, f"Target {TARGET} menit", fontsize=9)
for i, v in enumerate(nilai):
    kanan.text(v + 1, i, f"{v} mnt", va="center")                  # recognition over recall
kanan.set_title("SESUDAH: poli melewati target berwarna merah")
kanan.set_xlabel("Waktu tunggu rata-rata (menit)")
for sisi in ("top", "right"):
    kanan.spines[sisi].set_visible(False)                          # kurangi beban visual

plt.tight_layout()
plt.savefig("hasil_visualisasi.png", dpi=120)

lewat = [n for v, n in urut if v > TARGET]
print(f"Poli melewati target {TARGET} menit: {', '.join(lewat)}")
print("Gambar disimpan sebagai hasil_visualisasi.png")
