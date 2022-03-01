#Percabangan
a=30
b=10

if a>b:
    print("A lebih besar dari B")

c=100
d=100

if c>d:
    print("C lebih besar dari D")
elif c==d:
    print("Nilai C sama dengan nilai D ")

e=200
f=300

if e>f:
    print("E lebih besar dari F")
elif e==f:
    print("Nilai E sama dengan nilai F ")
else:
    print("Nilai F lebih besar dari nilai E")

h=100
i=150

if h>i:
    print("Nilai H lebih besar dari I")
else:
    print("Nilai I lebih besar dari ini H")

# Mempersingkat Penulisan If
if a>b: print("A lebih besar dari B")

print("Nilai H lebih besar dari I") if h>i else print("Nilai I lebih besar dari H")

print("E lebih besar dari F") if e>f else print ("Nilai F lebih besar dari nilai E") if e==f else print("Nilai E sama dengan nilai F ")

#Percabangan menggunakan Logika
a=300
b=20
c=10

if a>b and b>c:
    print ("Kondisi Tersebut Benar")

if a>b or c>b:
    print("Salah satu kondisi tersebut benar")

#Nested If
x=40

if x>10:
    print("X Lebih dari 10")
    if x>20:
        print("Dan X juga lebih dari 20")
    else:
        print("X tidak lebih dari 20")

#Pass Statement
if a>b:
    pass