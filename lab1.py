import math

def task1():
    try:
        num = int(input("Введіть тризначне число: "))
        if num < 100 or num > 999:
            raise ValueError("Число має бути тризначним!")
    except ValueError as e:
        print(e)
        return

    # Перетворюємо число на рядок, щоб маніпулювати цифрами
    num_str = str(num)
    # Переставляємо цифри
    result = int(num_str[1] + num_str[2] + num_str[0])
    print(f"Отримане число: {result}")

def task2():
    try:
        x = float(input("Введіть значення x: "))
    except ValueError:
        print("x має бути числом!")
        return

    try:
        # Перетворення кута в радіани
        radians_x = math.radians(x)
        radians_x_3 = math.radians(x**3)
        radians_x_64 = math.radians(x + 64)

        # Обчислення виразу
        numerator = 0.5 * math.sin(x**4)**2
        denominator = (math.sin(radians_x_64) * math.log(abs(x), 3))**0.5
        tangent_sin = math.tan(radians_x) * math.sin(radians_x_3)**2

        y = numerator / denominator / tangent_sin
        print(f"y = {y}")
    except Exception as e:
        print("Помилка в обчисленні виразу: ", e)

def task3():
    try:
        A = int(input("Введіть ціле позитивне число A: "))
        if A < 10 or A > 99:
            raise ValueError("Число має бути двозначним!")
    except ValueError as e:
        print(e)
        return

    # Перевірка на парність
    result = (A % 2 == 0)
    print(f"Число {A} є парним двозначним: {result}")

# Викликаємо функції для тестування
task1()
task2()
task3()
