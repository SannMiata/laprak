# DIBERIKAN LIST BERIKUT
kendaraan = ["motor", "mobil", "sepeda", "bus"]

# a. Tambahkan 'truk' di akhir list
kendaraan.append("truk")
print(kendaraan)


# b. Sisipkan becak' pada index ke-1
kendaraan.insert(1, "becak")
print(kendaraan)

# c. Hapus data yang berada paling belakang dari list tersebut.
kendaraan.pop()
print(kendaraan)

# d. Ubah elemen 'sepeda' menjadi 'skuter'.
kendaraan[2] = "skuter"
print(kendaraan)

# e. Tampilkan informasi jumlah total data di dalam list tersebut
panjang_kendaraan = len(kendaraan)
print(f"Jumlah total data: {panjang_kendaraan}")

# DIBERIKAN LIST BERIKUT
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada.
index_100 = angka.index(100)
print(f"Angka 100 berada pada index ke {index_100}")

# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
skor_75 = angka.count(75)
print(f"Jumlah siswa yang mendapatkan nilai 75 adalah {skor_75}")

# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.
print(f"Data sebelum diurutkan: \n{angka}")
angka.sort()
print(f"Data setelah diurutkan dari yang terkecil: \n{angka}")

# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
print(f"Data sebelum diurutkan: \n{angka}")
angka.sort()
print(f"Data setelah diurutkan dari yang terkecil: \n{angka}")
angka.reverse()
print(f"Data setelah diurutkan dari yang terbesar: \n{angka}")

# menu_utama = ["Nasi Goreng", "Mie Ayam"]
# menu_tambahan = ["Kerupuk", "Es Teh"]
# Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print(f"List sebelum digabungkan \n{menu_utama} dan {menu_tambahan}")
menu_utama.extend(menu_tambahan)
print(f"List setelah digabngkan \n{menu_utama}")

# Diberikan data nested list berupa informasi nama barang dan harganya:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
pensil = data_barang[1][1]
print(f"Nama barang dan harga: {data_barang[1][0]} {pensil}")

# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya.
for i in data_barang:
    print(f"Nama barang\t: {i[0]}")
    print(f"Harga barang\t: {i[1]}")
