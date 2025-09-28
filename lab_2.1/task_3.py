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

max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n

second_max = None
for n in numbers:
    if n != max_num:
        if second_max is None or n > second_max:
            second_max = n

print("Второе по величине число:", second_max)




