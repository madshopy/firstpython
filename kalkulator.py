

a = 25
b = 400

hasil = a * b

bayu = 60
budi = 58

# print('ipin membeli baju sebanyak =',a, 'dengan harga =',b, 'maka uang yang dikeluarkan sejumlah =', hasil )

print(f"ipin membeli celana sebanyak {a} dengan harga perbajunya itu {b} dollar maka uang yang dikeluarkan"
      f"oleh ipin yaitu {hasil} dolar")

# inputpengguna = (float(input("masukan nilai siswa = ")))

inputpengguna = (float(input(f"masukan nama siswa = ")))


if inputpengguna >= 70 :
    print("lulus terbaik")
elif inputpengguna >= 60 :
    print("belajar lagi")
else :
    print("tidak lulus")

