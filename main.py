"""
ini adalah demo project pertama python ku

"""
# a = "budi"
# b = 45000
# c = "hello world"
#
# print(c)
# print("ada seorang anak yang bernama",a,"membawa uang sebanyak",b)

import gempaterkini

from gempaterkini.gempaUPDATE.__init__ import bencana, gempaTerkini




# aplikasi gempa terkini folder utama (pembuatan secara prosedural)
if __name__ == '__main__':
    result = gempaterkini.exstrasi_data()
    gempaterkini.tampilkan_data(result)


## aplikasi gempa terkini subfolder (pembuatan secara OOP)
if __name__ == '__main__':
    gempa_indonesia = gempaTerkini("https://bmkg.go.id")
    print(f'Aplikasi Utama menggunakan package yang memiliki deskripsi {gempa_indonesia.description}')
    gempa_indonesia.tampilkan_keterangan()
    gempa_indonesia.run()
