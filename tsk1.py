# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Введите число: ')
summ = 0

for digit in number:
    if digit.isdigit():
        summ += int(digit)

print("Сумма цифр равна:", summ)