familiya = input("Фамилия: ")
imya = input("Имя: ")
otch = input("Отчество: ")

if familiya == "" or imya == "" or otch == "":
    print("Пожалуйста, заполните все поля!")
else:
    fio = f"{familiya} {imya[0]}.{otch[0]}."
    print("Итоговое значение:", fio)