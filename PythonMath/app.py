#Fungsi Matematika Bawaan
#Fungsi min()and max()dapat digunakan untuk menemukan nilai terendah atau tertinggi dalam iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#Fungsi abs()mengembalikan nilai absolut (positif) dari angka yang ditentukan:
x = abs(-7.25)

print(x)

#Fungsi mengembalikan nilai x ke pangkat y (x y ).pow(x, y)
x = pow(4, 3)

print(x)

#Python juga memiliki modul bawaan yang disebut math, yang memperluas daftar fungsi matematika.Untuk menggunakannya, Anda harus mengimpor mathmodul:
import math

x = math.sqrt(64)

print(x)

#Metode math.ceil()membulatkan angka ke atas ke bilangan bulat terdekat, dan math.floor() metode membulatkan angka ke bawah ke bilangan bulat terdekat, dan mengembalikan hasilnya:
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#Konstanta math.pi, mengembalikan nilai PI (3.14...):
import math

x = math.pi

print(x)

