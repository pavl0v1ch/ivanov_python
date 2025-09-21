text = input("Введите текст: ")

if text == "":
    print("Ошибка: поле ввода не может быть пустым.")
else:
    vowels = "aeiou"
    output = ""

    for symbol in text:
        if symbol.lower() not in vowels:
            output += symbol

    print("Итог:", output)