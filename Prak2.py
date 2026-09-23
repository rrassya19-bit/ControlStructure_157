angka1 = int(input("Masukkan Angka Pertama: "))
angka2 = int(input("Masukkan Angka Kedua: "))
angka3 = int(input("Masukkan Angka Ketiga: "))

if angka1 > angka2 and angka1 > angka3:
    print("Angka Pertama Adalah Angka Terbesar")
elif angka2 > angka1 and angka2 > angka3:
    print("Angka Kedua Adalah Angka Terbesar")
elif angka3 > angka1 and angka3 > angka2:
    print("Angka Ketiga Adalah Angka Terbesar")
else:
    print("Tidak Ada Angka Yang Terbesar")