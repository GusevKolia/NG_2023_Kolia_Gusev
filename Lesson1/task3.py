# Функція для додавання двох чисел
def add(x, y):
    return x + y

# Функція для віднімання двох чисел
def subtract(x, y):
    return x - y

# Функція для множення двох чисел
def multiply(x, y):
    return x * y

# Функція для ділення двох чисел
def divide(x, y):
    return x / y

# Вивід меню калькулятора
print("Виберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

# Зчитування вибору користувача
choice = input("Ваш вибір (1/2/3/4): ")

# Зчитування двох чисел
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Виклик функції в залежності від вибору користувача
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Невірний ввід")
