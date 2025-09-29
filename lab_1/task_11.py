day = int(input("День рождения: "))
month = int(input("Месяц рождения (число): "))

if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    print("Знак зодиака: Водолей")
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    print("Знак зодиака: Рыбы")
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Знак зодиака: Овен")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Знак зодиака: Телец")
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    print("Знак зодиака: Близнецы")
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    print("Знак зодиака: Рак")
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    print("Знак зодиака: Лев")
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    print("Знак зодиака: Дева")
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    print("Знак зодиака: Весы")
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    print("Знак зодиака: Скорпион")
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    print("Знак зодиака: Стрелец")
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    print("Знак зодиака: Козерог")
else:
    print("Некорректная дата")