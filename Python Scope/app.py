#Variabel yang dibuat di dalam fungsi tersedia di dalam fungsi itu:
def myfunc():
  x = 300
  print(x)

myfunc()

#Variabel lokal dapat diakses dari fungsi di dalam fungsi:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Variabel yang dibuat di luar fungsi bersifat global dan dapat digunakan oleh siapa saja:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#Fungsi akan mencetak local x, dan kemudian kode akan mencetak global x:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Jika Anda menggunakan globalkata kunci, variabel tersebut termasuk dalam lingkup global:
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#Untuk mengubah nilai variabel global di dalam suatu fungsi, lihat variabel tersebut dengan menggunakan globalkata kunci:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)