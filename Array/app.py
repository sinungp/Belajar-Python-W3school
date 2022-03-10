#Buat array yang berisi nama mobil
from distutils.command.clean import clean


cars = ["toyota","honda","suzuki"]

#Mendapatkan Nilai Array
print("Dapatkan nilai item array pertama")
x = cars[0]

print(x)

print("\n")
#Mengubah Nilai Array
cars[0] = "BMW"

print(cars[0])
print(cars)

print("\n")
#Panjang Array
print("Gunakan len()metode untuk mengembalikan panjang array (jumlah elemen dalam array).")
x = len(cars)

print(x)

print("\n")
#Perulangan
print("Anda dapat menggunakan for inloop untuk mengulang semua elemen array.")
for x in cars:
    print(x)

print("\n")
#Menambahkan Elemen Array
print("Anda dapat menggunakan append()metode untuk menambahkan elemen ke array.")
cars.append("Mercy")

print(cars)

print("\n")
#Menghapus Elemen Array
print("Anda dapat menggunakan pop()metode untuk menghapus elemen dari array.")
cars.pop(0)

print(cars)

