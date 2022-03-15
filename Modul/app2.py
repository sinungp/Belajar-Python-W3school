# import modul2

# a = modul2.person1["age"]
# print(a)

#Buat alias untuk mymoduledisebut mx:
import modul2 as mx

a = mx.person1["age"]
print(a)

#Ada beberapa modul bawaan dalam Python, yang dapat Anda impor kapan pun Anda mau.
import platform

x = platform.system()
print(x)

#Ada fungsi bawaan untuk mendaftar semua nama fungsi (atau nama variabel) dalam sebuah modul. Fungsi dir():
x = dir(platform)
print(x)

#Impor hanya kamus person1 dari modul:
from modul2 import person1

print (person1["age"])