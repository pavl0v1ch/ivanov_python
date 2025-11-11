parol = input("Пароль: ")

if parol == "":
    print("Ошибка: строка пуста.")
else:
    if len(parol) < 16:
        print("Пароль слишком короткий.")
    elif parol.isalpha() or parol.isdigit():
        print("Пароль недостаточно надёжный.")
    else:
        print("Пароль считается надёжным.")