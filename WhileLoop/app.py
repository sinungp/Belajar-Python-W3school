#While Loop
i=1
while i<6:
    print(i)
    i+=1

print("\n")
#Break Statement
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

print("\n")
#Continue Statement
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i) 

print("\n")
i=1
while i<6:
    print(i)
    i+=1
else:
    print("tidak ada yang lebih dari 6")