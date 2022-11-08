x = 1
sum = 0
Num_of_students = int(input("Wprowadz liczbe studentow: "))

if Num_of_students<1:
    exit()
while True:
    if x>Num_of_students:
        break
    points = int(input(f"Wprowadz liczbe punktow studenta {x}: "))
    if (points > 100 or points < 0):
        continue

    sum += points
    x+=1
median = sum/Num_of_students
print(("srednio puntow uczniow wynosi: "), median)