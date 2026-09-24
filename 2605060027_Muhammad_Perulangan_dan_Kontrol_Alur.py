# Program 5.1 For

# Perulangan (loop)
angka = 1
print(angka)

angka = angka + 1
print(angka)

angka = angka + 1
print(angka)

# Dengan list
angka2 = [0, 1, 2, 3, 4]
print(angka2)

for i in angka2:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")

# Dengan range
angka3 = range(5)

for i in angka3:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")

angka4 = range(1, 10)

for i in angka4:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")

# Menggunakan string
data_str = "saya ganteng abiies"

for huruf in data_str:
    print(huruf)

print("akhiri dari program\n")


# Program 5.2 While Loop

print("===contoh 1===")

angka = 10

while angka > 5:
    print("ipin lari ipin!!!")
    break

print("===contoh 2===")

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang → {angka}")
    print("ipin lari ipin")

print("program berakhir, ipin sudah jauh")


# Program 5.3 Continue and Pass

# pass
angka = 0

while angka < 5:
    angka = angka + 1

    if angka == 3:
        pass

    print(angka)

# continue
angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}")

    if angka == 3:
        print("nice")
        continue

    print("whasssup")

print("Pinish")


# Program 5.4 Break

angka = 0
print(f"angka sekarang → {angka}")

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang → {angka}")

    if angka == 3:
        print("nice")
        break

    print("whasssup")

print("cukup mass")


# Program 5.5 Latihan Perulangan

# Latihan membuat segitiga

# 1. Menggunakan for
sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan while
sisi = 4
count = 1

while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break


  # TUGAS
# 1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan!

for angka in range (1,51):
  if angka % 2 == 0:
    print(f"{angka} angka ini bilangan genap")
  else:
    print(f"{angka} angka ini bilangan ganjil")



# 2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan!

for angka in range(2, 101):
    cek_prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            cek_prima = False
            break

    if cek_prima:
        print(angka)