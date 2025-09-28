# Метод split() разбивает строку на отдельные элементы.
list1 = input("Введите первый набор чисел: ").split()

list2 = input("Введите второй набор чисел: ").split()

# Каждый элемент списка преобразуется в число.
# Если в строке есть точка это число с плавающей точкой (float), иначе — целое число (int).
list1 = [float(x) if "." in x else int(x) for x in list1]
list2 = [float(x) if "." in x else int(x) for x in list2]

common = []
only1 = []
only2 = []
exclusive = []

# Проход по первому списку:
# Если число присутствует во втором списке и ещё не добавлено в common — оно добавляется.
# Если число отсутствует во втором списке и ещё не добавлено в only1 — оно добавляется.
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
    elif x not in list2 and x not in only1:
        only1.append(x)

# Проход по второму списку:
# Добавляются числа, которых нет в первом списке и ещё нет в only2.
for x in list2:
    if x not in list1 and x not in only2:
        only2.append(x)

# Объединение двух списков:
# Проход по всем элементам из обоих списков.
# Если элемент не входит в список общих чисел и ещё не добавлен в exclusive — он добавляется.
for x in list1 + list2:
    if x not in common and x not in exclusive:
        exclusive.append(x)


print("Числа, которые есть в обоих наборах:", common)
print("Числа только из первого набора:", only1)
print("Числа только из второго набора:", only2)
print("Все числа, кроме общих:", exclusive)
