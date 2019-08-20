#  ----- КАЛЬКУЛЯТОР

import math


while True:

    what_do = input("Что делаем (+ , - , / , * , ** , % , унарный минус , округление , Пи): ")

    if what_do.lower() == "y":
        print("Программа завершена.")
        break

    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))


    if what_do == "+":
        c = a + b
        print("Результат: " + str(c))
    elif what_do == "-":
        c = a - b
        print("Результат: " + str(c))
    elif what_do == "/":
        c = a / b
        print("Результат: " + str(c))
    elif what_do == "*":
        c = a * b
        print("Результат: " + str(c))
    elif what_do == "**":
        c = a ** b
        print("Результат: " + str(c))
    elif what_do == "%":
        c = a % b
        print("Результат: " + str(c))
    elif what_do == "минус":
        c = -a
        d = -b
        print("Результат: " + str(c))
        print("Результат: " + str(d))
    elif what_do == "округ":
        c = round(a)
        d = round(b)
        print("Результат: " + str(c))
        print("Результат: " + str(d))
    elif what_do == "ПИ":
        c = a * math.pi
        d = b * math.pi
        print("Результат: " + str(c))
        print("Результат: " + str(d))
    else:
        print("Выбрана неверная операция!")

