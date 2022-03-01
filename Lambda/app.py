#Define Lambda
x=lambda a:a+10
print(x(5))

print("\n")
#Lambda functions can take any number of arguments:
x=lambda a,b:a+b
print(x(5,10))

print("\n")
#Summarize argument a, b, and c and return the result:
x=lambda a,b,c:a+b+c
print(x(5,5,5))

print("\n")
#Gunakan definisi fungsi itu untuk membuat fungsi yang selalu menggandakan nomor yang Anda kirim:
def fungsi(n):
    return lambda a:a*n

doubler = fungsi(2)
print(doubler(12))

print("\n")
#Atau, gunakan definisi fungsi yang sama untuk membuat fungsi yang selalu melipatgandakan jumlah yang Anda kirim:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print("\n")
#gunakan definisi fungsi yang sama untuk membuat kedua fungsi, dalam program yang sama:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))