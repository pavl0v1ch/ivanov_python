text = input("Введите числа через пробел: ")

numbers = []
num = ""
i = 0
while i < len(text):
    if text[i] != " ":
        num += text[i]
    else:
        if num != "":
            if "." in num:
                numbers.append(float(num))
            else:
                numbers.append(int(num))
            num = ""
    i += 1
if num != "":
    if "." in num:
        numbers.append(float(num))
    else:
        numbers.append(int(num))

unique = []
repeats = []
for n in numbers:
    if n not in unique:
        unique.append(n)
    else:
        if n not in repeats:
            repeats.append(n)

even = []
odd = []
for n in numbers:
    if isinstance(n, int):
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

negative = []
for n in numbers:
    if n < 0:
        negative.append(n)

floats = []
for n in numbers:
    if isinstance(n, float):
        floats.append(n)

sum_div_5 = 0
for n in numbers:
    if isinstance(n, int) and n % 5 == 0:
        sum_div_5 += n

max_num = numbers[0]
min_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Уникальные числа:", unique)
print("Повторяющиеся числа:", repeats)
print("Чётные числа:", even)
print("Нечётные числа:", odd)
print("Отрицательные числа:", negative)
print("Числа с плавающей точкой:", floats)
print("Сумма чисел, кратных 5:", sum_div_5)
print("Самое большое число:", max_num)
print("Самое маленькое число:", min_num)

