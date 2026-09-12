# operasi logika atau boolean
# not, or, and, xor

print('===NOT===')
a = True
b = not a
print(' data a=', a)
print('---- NOT')
print('data b =', b)


# OR (jika salah satu true, maka hasilnya adalah true)
print('===OR===')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)


# AND (jika dua buah nilai true, maka hasil true)
print('===AND===')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)


# XOR (akan true jika salah satu true, sisanya false)
print('===XOR===')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)


# latihan logika dan komparasi
# membuat gabungan area rentang dari angka
# ++++++3--------10++++++

inputUser = float(input('masukkan angka yang bernilai\nkurang dari 3 \natau\nlebih besar dari 10\n:'))


# ++++++3--------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 =', isKurangDari)


# --------10++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('Lebih dari 10 =', isLebihDari)
isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukkan: ', isCorrect)

print('========================================')

# -------3++++++10-------
# khusus irisan

inputUser = float(input('masukkan angka yang bernilai\nlebih dari 3 \ndan\nkurang dari 10\n:'))
# ----3++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print('Lebih dari 3 = ', isLebihDari)

# +++++++10------
# kurang dari 10
isKurangDari = inputUser < 10
print('Kurang daru 10 = ', isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan: ', isCorrect)


# if dan else statement
# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input('Siapa nama anda? ')

# 1. Program if inline
if nama =='ucup':print('Kamu Ganteng abieeezz!!!!')
print('akhir dari program')

# 2. Program if identation
if nama =='ucup':
  print('kamu ganteng abiiez!')
  print('kamu juga keren banget')
print('akhir daru program')

# 3. Else statement
if nama=='paijo':
  print('ah kamu bukan paijo, kamu gak keren')
print('akhir dari program')


# Elif = else if statement

nama = input('Siapa nama anda? ')

# if kondisi:
# aksi true
# elif kondisi:
#aksi true
# elif kondisi:
#aksi true
# else:
#aksi

if nama == 'ucup': # kondisi 1
  print('hai gabteng abiiz!!!') # aksi true 1
elif nama == 'paijo': # kondisi 2
  print('hai si kece bangeets!!!') # aksi true 2
elif nama == 'mario': # kondisi 3
  print('hai humoris!!!') # aksi true 3
else:
  print('wtf gak kenal!!!') # aksi false
print ('akhir program')


# Penugasan
#Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia 
# tersebut berdasarkan kriteria berikut:
# 0 - 12 tahun: Anak-anak
# 13 - 17 tahun: Remaja
# 18 - 59 tahun: Dewasa
# 60 tahun ke atas: lansia

# Program kategori usia

usia = int(input("Masukkan usia anda: "))

if usia >= 0 and usia <= 12:
    print("Kategori: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori: Remaja")
elif usia >= 18 and usia <= 59:
    print("Kategori: Dewasa")
elif usia >= 60:
    print("Kategori: Lansia")
else:
    print("Usia tidak valid")

print("Akhir dari program")