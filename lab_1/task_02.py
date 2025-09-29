string = input("Введите строку:")

if string.strip() == "":
    print("Пустая строка")
else:
    vowels = "aeiouAEIOU"
    table = str.maketrans("", "", vowels)
    result = string.translate(table)
    print("Результат:", result)
