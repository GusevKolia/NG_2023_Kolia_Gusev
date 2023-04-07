import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("The equation has no real roots.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"The equation has one root: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"The equation has two roots: x1 = {x1}, x2 = {x2}")
