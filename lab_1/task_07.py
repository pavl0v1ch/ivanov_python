sec = int(input("Введите количество секунд: "))
min = sec // 60
sec_left = sec % 60

print(f"{min}:{sec_left}")