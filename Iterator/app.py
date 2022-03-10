#Kembalikan iterator dari Tuple, dan cetak setiap nilai:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#String juga merupakan objek yang dapat diubah, berisi urutan karakter:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Iterasi nilai tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Iterasi karakter string:
mystr = "banana"

for x in mystr:
  print(x)

#Buat iterator yang mengembalikan angka, dimulai dengan 1, dan setiap urutan akan bertambah satu (mengembalikan 1,2,3,4,5 dll.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Berhenti setelah 20 iterasi:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

