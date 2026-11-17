import datetime   # Untuk menyimpan tanggal/waktu
import os         # Untuk membersihkan layar terminal
import string     # Untuk mengambil huruf A-Z
import random     # Untuk mengacak huruf pada KEY

# Template data buku
buku = {
    "judul": 'judul',
    "penulis": 'penulis',
    "tahun": 0,
    "terakhir": datetime.datetime(1111, 1, 11),
    "status": 'TERSEDIA',

}
# Nesting Dictionary untuk menampung seluruh buku.
data_buku = {}

while True:
    # os.system("cls") # Untuk WIN
    system("clear") # Untuk LIN/MAC
    
# Judul input
    print(f"{'SELAMAT DATANG DI E-PERPUS':^20}")
    print(f"{'DATA BUKU':^20}")


# Input data buku
    buku['judul'] = input("Masukkan Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun'] = input("Tahun Terbit: ")

# Input data waktu
    TAHUN_PINJAM = int(input("Tahun terakhir pinjam: "))
    BULAN_PINJAM = int(input("Bulan terakhir pinjam: "))
    TANGGAL_PINJAM = int(input("Tanggal terakhir pinjam: "))
    buku['tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)

# Input status buku
    buku['status'] = input("Status (TERSEDIA / TIDAK): ").upper()

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_buku.update({KEY: buku})


# Menampilkan data ke dalam tabel
    print(f"\n{'KEY':<8} {'Judul':<20} {'Penulis':<17} {'Terbit':<6} {'Terakhir Pinjam':<16} {'Status':<9}")
    print('-' * 80)

    for KEY in data_buku:
        BUKU = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TERBIT = data_buku[KEY]['tahun']
        TERAKHIR = data_buku[KEY]['tanggal_pinjam'].strftime("%x")
        STATUS = data_buku[KEY]['status']
        print(f"{KEY:<8} {BUKU:<20} {PENULIS:<17} {TERBIT:<6} {TERAKHIR:<16} {STATUS:<9}")

# Konfirmasi pengguna
    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")
