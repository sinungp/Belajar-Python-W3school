#Jika Anda memiliki string JSON, Anda dapat menguraikannya dengan menggunakan json.loads()metode.
#Konversi dari JSON ke Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Jika Anda memiliki objek Python, Anda dapat mengubahnya menjadi string JSON dengan menggunakan json.dumps()metode.
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Ubah objek Python menjadi string JSON, dan cetak nilainya:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Mengonversi objek Python yang berisi semua tipe data legal:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#Gunakan indentparameter untuk menentukan jumlah indentasi:
print(json.dumps(x, indent=4))

#Gunakan separatorsparameter untuk mengubah pemisah default:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Gunakan sort_keysparameter untuk menentukan apakah hasilnya harus diurutkan atau tidak:
print(json.dumps(x, indent=4, sort_keys=True))

