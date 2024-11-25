"""
pengulanaan while
program membaca buku
"""

#pengulangan while memiliki kelebihan untuk mengulang suatu kondisi nilai boolean

totalbuku = 10
print("baca dan pahami semua bukumu")
total_dibaca = 0

jumlah_paham = 0
# print(f"buku yang sudah dipahami {buku_sudah_paham}")

while total_dibaca < totalbuku:
    total_dibaca = total_dibaca + 1
    print(f"buku ke - {total_dibaca} sudah dibaca dan dipahami")
    if jumlah_paham == 9 :
        print(f"buku ke - {jumlah_paham + 1 } belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"buku ke - {jumlah_paham+1} sudah dibaca dan dipahami")

print(f"total buku yang sudah dibaca dan dipahami {jumlah_paham}")
if jumlah_paham == totalbuku:
    print('"Bu, semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, tidak semua buku bisa dipahami. '
          f'Aku hanya bisa memahami {jumlah_paham}"')

