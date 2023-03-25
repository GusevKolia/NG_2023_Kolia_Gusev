import math

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

if a == 0:
    print("Це не квадратне рівняння.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Рівняння не має дійсних коренів.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Рівняння має один корінь: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Рівняння має два корені: x1 = {x1}, x2 = {x2}")