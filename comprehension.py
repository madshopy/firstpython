print("\n Membuat list baru")
pelajaran = ['kimia','ipa','tik','english','agama']
data_pelajaran =  pelajaran[:]
del pelajaran[:] # menghapus secara comprehension/semua variabel

for i in range(0, len(data_pelajaran)):
    print(data_pelajaran[i])
print(pelajaran) # menjadi kosong


print("\n Membuat list baru")
matapelajaran = ['kimia','ipa','tik','english','agama']

for i in range(0, len(matapelajaran)):
    print(matapelajaran[i])

print("\n Membuat list baru dengan comprehension ganjil")
matapelajaran = ['0 kimia', '1 ipa', '2 tik', '3 english', '4 agama']
pelajaran = matapelajaran[1::2]

for i in range(0, len(pelajaran)):
        print(pelajaran[i])

print("\n Membuat list baru dengan comprehension genap")
matapelajaran = ['0 kimia', '1 ipa', '2 tik', '3 english', '4 agama']
pelajaran = matapelajaran[0::2]

for i in range(0, len(pelajaran)):
        print(pelajaran[i])

print("\n Membuat list baru dengan comprehension buang ujung")
matapelajaran = ['0 kimia', '1 ipa', '2 tik', '3 english', '4 agama']
pelajaran = matapelajaran[0:-1:2]

for i in range(0, len(pelajaran)):
        print(pelajaran[i])

print("\n Membuat list baru dengan comprehension pemanggilan cepat tanpa buat variabel baru")
matapelajaran = ['0 kimia', '1 ipa', '2 tik', '3 english', '4 agama']
print(matapelajaran[1::2])
