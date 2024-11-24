#latihan konversi satuan suhu

print("\nKONVERSI TEMPERATUR SUHU FAHRENHEIT\n")

#konversi suhu fahrenheit ke satuan lain
fahrenheit = float(input('masukan suhu dalam fahrenheit' ))
print('suhu adalah',fahrenheit,'derajat fahrenheit')

#reamur
reamur = (4/9) * (fahrenheit-32)
print('konversi ke satuan suhu reamur adalah = ',reamur,'derajat reamur')

#cecius
celcius = (5/9) * (fahrenheit-32)
print('konversi ke satuan suhu celcius adalah = ',celcius,'derajat celcius')

#kelvin
kelvin = (fahrenheit-32) * (5/9) + 273
print('konversi ke satuan suhu kelvin adalah = ',kelvin,'derajat kelvin')



print("\nKONVERSI TEMPERATUR SUHU KELVIN\n")

#konversi suhu KELVIN ke satuan lain
kelvin2 = float(input('masukan suhu dalam kelvin' ))
print('suhu adalah',kelvin2,'derajat kelvin')

#reamur
reamur2 = (4/5) * (kelvin2-273)
print('konversi ke satuan suhu reamur adalah = ',reamur2,'derajat reamur')

#cecius
celcius2 = kelvin2 - 273
print('konversi ke satuan suhu celcius adalah = ',celcius2,'derajat celcius')

#fahrenheit
fahrenheit2 = (kelvin2-273)*(9/5)+273
print('konversi ke satuan suhu fahrenheit adalah = ',fahrenheit2,'derajat fahrenheit')