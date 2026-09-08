# Operasi aritmatika dan komperasi

# 3.1
# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)


# 3.2
# latihan konversi satuan temperature
# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))

print("Suhu adalah", celcius, "Celcius")

# reamur
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah", kelvin, "Kelvin")

# 3.3
# operasi komperasi
# setiap hasil dari operasi komperasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
print("=============== lebih besar dari (>)")

hasil = a > 3
print(a, '>', b, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

hasil = b > 2
print(b, '>', 2, '=', hasil)

# kurang dari <
print("=============== kurang dari (<)")

hasil = a < 3
print(a, '<', b, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih dari sama dengan >=
print("=============== lebih besar sama dengan (>=)")

hasil = a >= 3
print(a, '>=', b, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")

hasil = a <= 3
print(a, '<=', b, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan (==)
print("=============== sama dengan (==)")

hasil = a == 4
print(a, '==', 4, '=', hasil)

hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidak sama dengan (!=)
print("=============== tidak sama dengan (!=)")

hasil = a != 4
print(a, '!=', 4, '=', hasil)

hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi object identity
# (bukan literal)
x = 5
y = 5

hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi object identity
# (bukan literal)
x = 5
y = 6

hasil = x is not y
print('x is not y =', hasil)




# Tugas
panjang = 12
lebar = 5
tinggi = 8

# Soal 1, Hitunglah luas, volume dan keliling dari bangunan tersebut!
print("Luas dari balok dapat dihitung menggunakan rumus L= 2*(p*l + p*t + l*t)")
luas = 2*(panjang*lebar + panjang*tinggi + lebar*tinggi)
print("Jadi, luas dari bangun tersebut L= 2*(12*5 + 12*8 + 5*8) hasilnya", luas)
print()

print("Volume dari balok dapat dihitung menggunakan rumus V= p*l*t")
volume = panjang*lebar*tinggi
print("Jadi, volume bangun tersebut adalah V= 12*5*8 hasilnya", volume)
print()

print("Keliling dari balok dapat dihitung menggunakan rumus K= 4*(p+l+t)")
keliling = 4*(panjang+lebar+tinggi)
print("Jadi, keliling bangun tersebut adalah K= 4*(12+5+8) hasilnya", keliling)
print()

# Soal 2, Apakah luas bangunan tersebut lebih luas dari 50?
jawab_b = luas > 50
print("Apakah luas lebih dari 50? ", jawab_b)
print()

# Soal 3, Apakah volume tersebut bernilai 480?
jawab_c = volume == 480
print("Apakah volume bernilai 480? ", jawab_c)
