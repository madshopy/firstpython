"""
semua sintaks dasar pemrograman terdiri dari
1. sekunsial    : langkah berurutan
2. percabangan  : langkah lompat bila kondisi terpenuhi
3. perulangan   : mengulang langkah yang sama berulang-ulang kali sampai kondisi terpenuhi

"""

#sekuensial
print('ibu berkata "belikan ibu susu 1 botol dan apabila ada telur beli kan telur 6"')
print('anak menjawab "ok" ')

#percabangan
susu = 150
telur = 2005

print("\nwelcome to toko sembako")
print("_"*30)

print(f"stok susu saat ini : {susu}")
print(f"stok telur saat ini : {telur}")

if susu > 0 :
    print('anak : "apakah ada susu" ?')
    print(f'penjual menjawab : "stok susu ada" {susu} botol ')
    print("beli susu satu botol")
else :
    print("tidak membeli susu")

if telur > 0 :
    print('anak : "apakah ada telur" ?')
    print(f'penjual menjawab : "stok telur ada {telur} butir"')  # f berfungsi untuk meletakan varibale dalam text print
    print("beli telur 6 butir")
else :
    print(" hanya membeli susu")

print("anak pulang ke rumah dan menyerahkan hasil belanjanya kepada si ibu")
print("selesai")


print()