import datetime
import os
import string
import random

buku = {
    "judul": 'judul',
    "penulis": 'penulis',
    "tahun": 0,
    "terakhir": datetime.datetime(1111, 1, 11),
    "status": 'TERSEDIA',

}

data_buku = {}

while True:
    os.system("cls") # Untuk WIN
    os.system("clear") # Untuk LIN/MAC

    print(f"{'SELAMAT DATANG DI E-PERPUS':^20}")
    print(f"{'DATA PERPUSTAKAAN':^20}")

    buku['judul'] = input("Masukkan Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun'] = input("Tahun Terbit: ")
    TAHUN_PINJAM = int(input("Tahun terakhir pinjam: "))
    BULAN_PINJAM = int(input("Bulan terakhir pinjam: "))
    TANGGAL_PINJAM = int(input("Tanggal terakhir pinjam: "))
    buku['tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    buku['status'] = input("Status (TERSEDIA / TIDAK): ").upper()

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_buku.update({KEY: buku})

    print(f"\n{'KEY':<8} {'Judul':<20} {'Penulis':<17} {'Tahun':<6} {'Terakhir Pinjam':<16} {'Status':<9}")
    print('-' * 80)

    for KEY in data_buku:
        JUDUL = data_buku[KEY]['judul']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun']
        PINJAM = data_buku[KEY]['tanggal_pinjam'].strftime("%x")
        STATUS = data_buku[KEY]['status']
        print(f"{KEY:<8} {JUDUL:<20} {PENULIS:<17} {TAHUN:<6} {PINJAM:<16} {STATUS:<9}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")
