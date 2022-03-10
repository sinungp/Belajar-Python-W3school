#Untuk membuat kelas, gunakan kata kunci class:
class kelasku:
    x=5

#Buat objek bernama p1, dan cetak nilai x:
p1 = kelasku()
print(p1.x)

#Buat kelas bernama Person, gunakan fungsi __init__() untuk menetapkan nilai untuk nama dan usia:
class orang:
    def __init__(self, nama, umur) :
        self.nama = nama
        self.umur = umur

p1 = orang("Sinung",22)

print(p1.nama)
print(p1.umur)

#Sisipkan fungsi yang mencetak salam, dan jalankan pada objek p1:
class orang:
    def __init__(self, nama, umur):
        self.nama=nama
        self.umur=umur

    def fungsiku(self):
        print("Halo nama saya adalah "+self.nama)
    
p1=orang("Sinung",22)
p1.fungsiku()

#Belajar Membuat Class
class Mahasiswa:
  def __init__(self,nama,nim,prodi,thn_masuk):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.thn_masuk = thn_masuk

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(m1.nama,m1.prodi,m1.thn_masuk,m1.nim)
print(teks)

