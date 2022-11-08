import random
n = int(input("wporwadz liczbe: "))
zestaw_1=[]
for i in range(n):
    zestaw_1.append(random.randrange(1, 11))
    n+=1
print(zestaw_1)

zestaw_2=[]
m = int(input("wporwadz liczbe: "))
for i in range(m):
    zestaw_2.append(random.randrange(5, 16))
    n+=1
print(zestaw_2)
t = int(input("jako liczbe pan/pani szuka?"))
if t in zestaw_1 or:
    print("liczba jest w zbiorze 1")
elif t in zestaw_2:
    print("liczba jest w zbiorze 1")
else:
    print("liczby nie znaleziona")