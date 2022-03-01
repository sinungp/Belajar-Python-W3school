#For Loop
buah=["melon","jambu","jeruk"]
for x in buah:
    print(x)

print("\n")
#Looping melalui string
for y in "banana":
    print(y)

print("\n")
#Break statement
for x in buah:
    print(x)
    if x == "jambu":
        break

print("\n")
#Continue statement
for x in buah:
    if x == "jambu":
        continue
    print(x)

print("\n")
#Range Function
for x in range(6):
    print(x)

print("\n")
for x in range(2,6):
    print(x)

print("\n")
for x in range(2, 30 ,3):
    print(x)

print("\n")
#For Loop with else func
for x in range(6):
    print(x)
else:
    print("Akhirnya selesai")

print("\n")
for x in range(6):
    if x==3: break
    print(x)
else:
    print("Akhirnya selesai")

print("\n")
ciri=["merah","besar","enak"]
buah=["apel","pisang","ceri"]

for x in ciri:
    for y in buah:
        print(x,y)

print("\n")
#pass statement
for x in(0,1,2):
    pass