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
