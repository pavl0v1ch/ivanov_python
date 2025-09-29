stroka = input("Введите текст: ")

if stroka == "":
    print("Ошибка: строка пуста.")
else:
    normalized = stroka.lower()
    reversed_text = normalized[::-1]

    if normalized == reversed_text:
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")