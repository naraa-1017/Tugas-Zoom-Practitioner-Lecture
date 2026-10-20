import numpy as np
from mpi4py import MPI


KAPASITAS_SUNGAI = 220       # debit maksimum sebelum meluap (m3/detik)
AMBANG_SIAGA = 5.0           # peluang banjir (%) untuk status SIAGA
TOTAL_SIMULASI = 8_000_000   # jumlah skenario (Tahap 2)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()       # nomor proses ini
size = comm.Get_size()       # jumlah proses seluruhnya


def simulasi(n, seed):
    """Hitung berapa dari n skenario yang menyebabkan banjir."""
    rng = np.random.default_rng(seed)
    hujan = rng.gamma(shape=2.0, scale=40.0, size=n)     # curah hujan (distribusi gamma)
    tanah_jenuh = rng.uniform(0.3, 1.0, size=n)          # kejenuhan tanah 30%-100%
    debit = hujan * tanah_jenuh * 1.6                    # debit sungai
    return int((debit > KAPASITAS_SUNGAI).sum())



comm.Barrier()
mulai = MPI.Wtime()
banjir_lokal = simulasi(TOTAL_SIMULASI // size, seed=rank)      # tiap proses bekerja
banjir_total = comm.reduce(banjir_lokal, op=MPI.SUM, root=0)    # gabungkan hasil
comm.Barrier()
waktu = MPI.Wtime() - mulai


if rank == 0:
    total = (TOTAL_SIMULASI // size) * size
    peluang = banjir_total / total * 100
    status = "SIAGA" if peluang > AMBANG_SIAGA else "AMAN"

    print("=== Simulasi Risiko Banjir Kota dengan HPC (MPI) ===")
    print(f"Jumlah proses MPI : {size}")
    print(f"Jumlah skenario   : {total:,}")
    print(f"Peluang banjir    : {peluang:.2f}%")
    print(f"Waktu komputasi   : {waktu:.2f} detik")
    print(f"Status            : {status}")
    if status == "SIAGA":
        print("Rekomendasi       : siapkan pompa, posko, dan jalur evakuasi")
    else:
        print("Rekomendasi       : pantau terus curah hujan dan debit sungai")
