# Literal Data

# 2.1
# Menampilkan teks ke konsol
print("Hello World")

# Membuat variabel
a = 10
x = 5
panjang = 1000

# Menampilkan nilai variabel
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)


# 2.2
# Integer: bilangan bulat
data_integer = 1
print("Data:", data_integer)
print("Tipe:", type(data_integer))

# Float: bilangan desimal
data_float = 1.5
print("Data:", data_float)
print("Tipe:", type(data_float))

# String: kumpulan karakter
data_string = "ucup"
print("Data:", data_string)
print("Tipe:", type(data_string))

# Boolean: True atau False
data_bool = True
print("Data:", data_bool)
print("Tipe:", type(data_bool))

# Complex: bilangan kompleks
data_complex = complex(5, 6)
print("Data:", data_complex)
print("Tipe:", type(data_complex))

# 2.3
# Contoh penamaan variabel
nilai_y = 15
juta10 = 10000000
nilaiZ = 17.5

# Membuat variabel
a = 10
print("Nilai a =", a)

# Mengubah nilai variabel
a = 7
print("Nilai a =", a)

# Assignment tidak langsung
b = a
print("Nilai b =", b)


# TUGAS NOMOR 1
nama = "Muhammad Ichsan"     # nama → string
umur = 19                     # umur → integer
berat = 55.4                 # berat → float

print("Nama    :", nama)            # menampilkan variabel nama
print("Umur    :", umur, "tahun")   # menampilkan variabel umur
print("Berat   :", berat, "kg")     # menampilkan variabel berat


# TUGAS NOMOR 2
# mengubah tipe dibawah ini
angka_string = "123"         # string
angka_float = 45.67          # float
angka_integer = 89           # integer

# menjadi ini
h1 = int(angka_string)     # input dari "123" akan berubah menjadi 123
h2 = int(angka_float)      # input dari 45.67 akan berubah menjadi 45
h3 = float(angka_integer)  # input dari 89 akan berubah menjadi 89.0
h4 = str(angka_integer)    # input dari 89 akan berubah menjadi 89

# hasilnya 
print("data: ", (h1), "type", type(h1))  # menampilkan hasil dan tipe
print("data: ", (h2), "type", type(h2))  # menampilkan hasil dan tipe
print("data: ", (h3), "type", type(h3))  # menampilkan hasil dan tipe 
print("data: ", (h4), "type", type(h4))  # menampilkan hasil dan tipe

# TUGAS NOMOR 3
usia = int(input("Masukkan usia anda :"))              # Meminta input usia (integer)
tinggi = float(input("Masukkan tinggi badan anda :"))  # Meminta input tinggi badan (float)
nama = input("Masukkan nama anda :")                   # Meminta input nama (string)

# hasil
print("Nama          : ", (nama))   # menampilkan hasil nama
print("Usia          : ", (usia))   # menampilkan hasil usia
print("Tinggi badan  : ", (tinggi)) # menampilkan hasil tinggi
