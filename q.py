# print("Hi Andrew!")

# # int (integer)
# number = 5
#
# # float
# fnumber = 5.7
#
# # str (string)
# name = "Andrew"
# symbol = "*"
#
# # bool
# status = True

# print("что нужно вывести на экран")

# print("Он \"плохой\" человек или нет")
#
# print('Он "плохой" человек или нет')
#
# print("Он 'плохой' человек или нет")
#
# print("привет\nмир")

# ----- Конкатенация

# print("Привет, меня зовут  " + name)
#
# print("пароль" + symbol)

# print("Мой возраст " + str(number+fnumber) + " года!")

# ----- INPUT

# name_input = input("Введите свое имя:")
# age_input = input("Укажите Ваш возраст:")
# age_input = int(age_input)
# age_two = 2
# print("Привет " + name_input + " !")
# print("Тебе уже " + str(age_input + age_two) + " года и это круто !!!")


# ---- + , - , / , * , ** , % , унарный минус , округление , Пи
#
# a = 5
# b = 10
#
# a = -a
# c = b-a
#
# print(c)

# import math
#
#
# d=5.49
# print(math.pi)


#  ----- КАЛЬКУЛЯТОР

import math
from colorama import init
# from colorama import Fore, Back, Style

# init()

# print(Fore.BLACK)
# print(Back.LIGHTBLUE_EX)

what_do = input("Что делаем (+ , - , / , * , ** , % , унарный минус , округление , Пи): ")
# print(Fore.BLACK)
# print(Back.BLUE)

a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))

# print(Fore.BLACK)
# print(Back.YELLOW)

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

input()
