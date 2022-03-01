#Membuat Fungsi
def fungsi_saya():
    print("Halo Fungsi")

#Memanggil Fungsi
def fungsi():
    print("Halo Fungsi")

fungsi()

print("\n")
#Argument
def fungsi_nama(fnama):
    print(fnama+"dan aku")

fungsi_nama("Aa ")
fungsi_nama("Bb ")
fungsi_nama("Cc ")

print("\n")
#Argumen Angka
def fungsi_nama(namadepan, namabelakang):
    print(namadepan+" "+namabelakang)

fungsi_nama("sinung", "prayetno")

print("\n")
#Arbitary Argument
def fungsi_nama(*anak):
    print("Nama anak kamu adalah "+anak[0])

fungsi_nama("A","B","C")

print("\n")
#keyword Argument
def fungsi_nama(anak3,anak2,anak1):
    print("Nama anak kamu adalah "+anak2)

fungsi_nama(anak1="A", anak2="B", anak3="C")

print("\n")
#Arbitary Keyword Argument
def fungsi_nama(**anak):
    print("Nama akhir anak mu adalah "+anak["namaakhir"])

fungsi_nama(namadepan="AAA", namaakhir="BBB")

print("\n")
#Default Parameter Value
def fungsi_saya(negara="Swedia"):
    print("Negara saya adalah "+negara)

fungsi_saya()
fungsi_saya("Amerika")
fungsi_saya("Indonesia")
fungsi_saya("Jepang")

print("\n")
#Passing List as an argument
def fungsi_saya(makanan):
    for x in makanan:
        print(x)

makanan=["nasi","ikan","ayam"]

fungsi_saya(makanan)

print("\n")
#Return Values
def fungsi_saya(x):
    return 5*x

print(fungsi_saya(3))
print(fungsi_saya(10))
print(fungsi_saya(7))

#Pass Function
def fungsi_saya(x):
    pass

print("\n")
#Rekursif
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


