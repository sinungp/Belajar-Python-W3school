#Tanggal dalam Python bukanlah tipe datanya sendiri, tetapi kita dapat mengimpor modul bernama datetimeuntuk bekerja dengan tanggal sebagai objek tanggal.
#Impor modul datetime dan tampilkan tanggal saat ini:
import datetime

x = datetime.datetime.now()
print(x)

#Kembalikan tahun dan nama hari kerja:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#Untuk membuat tanggal, kita dapat menggunakan datetime()kelas (konstruktor) dari datetimemodul.Kelas datetime()membutuhkan tiga parameter untuk membuat tanggal: tahun, bulan, hari.
#Buat objek tanggal:
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#Metode strftime()
#Objek datetimememiliki metode untuk memformat objek tanggal menjadi string yang dapat dibaca.

#Metode ini dipanggil strftime(), dan mengambil satu parameter, format, untuk menentukan format string yang dikembalikan:
#Menampilkan nama bulan:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

