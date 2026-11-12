# # Latihan 1 - Tuple
# #
# #  a. Tuple
# mahasiswa = ("Budi Santoso", "240101", "Teknologi Informasi")

# # b. Akses NIM dan Prodi lewat indeks
# print(mahasiswa[1])   # NIM
# print(mahasiswa[2])   # Prodi

# # c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi".
# mahasiswa[2] = "Teknologi Informasi"


# # d. Set
# nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
# print(nilai_angka)




# # Latihan 2 - Manipulasi Dictionary
# #
# # a.  Dictionary bernama data_mahasiswa dengan pasangan key-value.
# data_mahasiswa = {
#     "nim": "240101",
#     "nama": "Budi Santoso",
#     "prodi": "Teknologi Informasi"
# }

# # b. Ubah prodi + tambah angkatan dengan nilai 2026
# data_mahasiswa["prodi"] = "Sastra Mesin"
# data_mahasiswa["angkatan"] = 2026

# # c. Hapus nim lalu tampilkan
# del data_mahasiswa["nim"]
# print(data_mahasiswa)



# Latihan 3 - Perulangan pada Dictionary
#
# a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel":5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}

# b. Tampilkan tiap barang dan harga
for buah, harga in keranjang.items():
    print(f"Harga Buah {buah}: Rp {harga}")

# c. Total belanja
total = 0
for harga in keranjang.values():
    total = total + harga

print(f"Total belanja: Rp {total}")
