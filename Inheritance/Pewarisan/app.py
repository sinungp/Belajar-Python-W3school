#Buat kelas bernama Person, dengan firstnamedan lastnameproperti, dan printnamemetode:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Buat kelas bernama Student, yang akan mewarisi properti dan metode dari Personkelas:
class Student(Person):
    pass
#Gunakan Studentkelas untuk membuat objek, lalu jalankan printnamemetode:
x = Student("Mike", "Olsen")
x.printname()

#Untuk mempertahankan pewarisan fungsi induk __init__() , tambahkan panggilan ke fungsi induk __init__():
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#Dengan menggunakan super()fungsi, Anda tidak harus menggunakan nama elemen induk, secara otomatis akan mewarisi metode dan properti dari induknya.
#Tambahkan properti yang dipanggil graduationyearke Studentkelas:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

#Tambahkan yearparameter, dan berikan tahun yang benar saat membuat objek:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

#Tambahkan metode yang dipanggil welcomeke Studentkelas:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

