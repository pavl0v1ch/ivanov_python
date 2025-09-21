number = int(input("Введите число: "))

if number % 7 == 0:
    print("Магическое число!")
else:
    summa = sum(int(digit) for digit in str(number))
    print("Сумма цифр:", summa)