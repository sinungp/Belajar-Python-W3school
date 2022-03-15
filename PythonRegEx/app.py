#Python memiliki paket bawaan yang disebut re, yang dapat digunakan untuk bekerja dengan Ekspresi Reguler.
#Cari string untuk melihat apakah itu dimulai dengan "The" dan diakhiri dengan "Spanyol":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#Fungsi findall()mengembalikan daftar yang berisi semua kecocokan.
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Kembalikan daftar kosong jika tidak ditemukan kecocokan:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#Fungsi search()mencari string untuk kecocokan, dan mengembalikan objek Match jika ada kecocokan.
#Jika ada lebih dari satu kecocokan, hanya kemunculan pertama kecocokan yang akan dikembalikan:
#Cari karakter spasi putih pertama dalam string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Fungsi split()mengembalikan daftar tempat string telah dipisah pada setiap kecocokan:
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Anda dapat mengontrol jumlah kemunculan dengan menentukan maxsplit parameter:
#Pisahkan string hanya pada kemunculan pertama:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#Fungsinya sub()menggantikan kecocokan dengan teks pilihan Anda:
#Ganti setiap karakter spasi putih dengan angka 9:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Anda dapat mengontrol jumlah penggantian dengan menentukan count parameter:
#Ganti 2 kejadian pertama:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Lakukan pencarian yang akan mengembalikan Objek yang Cocok:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Cetak posisi (posisi awal dan akhir) dari kejadian kecocokan pertama.
#Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Cetak string yang diteruskan ke fungsi:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


#Cetak bagian string di mana ada kecocokan.
#Ekspresi reguler mencari kata apa pun yang dimulai dengan huruf besar "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())



