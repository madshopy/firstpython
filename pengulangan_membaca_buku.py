"""
program pengulangan membaca buku
"""

# pengulangan for
#digunakan untuk mengulang suatu kondisi yang telah diketahui total jumlahnya

total_buku = 100
print(f"ibu memerintahkan membaca buku di perpustakaan ")
print("_"*30)

buku_sudah_dibaca = 0

for buku_sudah_dibaca in range (1, total_buku+1) :
    print(f"buku ke -{buku_sudah_dibaca} sudah dibaca")

print(f"total buku yang sudah dibaca sebanyak {buku_sudah_dibaca} buah")


