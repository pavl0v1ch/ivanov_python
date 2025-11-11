familiya = input("Фамилия: ")
imya = input("Имя: ")
otch = input("Отчество: ")

if familiya == "" or imya == "" or otch == "":
    print("Пожалуйста, заполните все поля!")
else:
    print(f"Итоговое значение: {familiya} {imya[0]}.{otch[0]}.")