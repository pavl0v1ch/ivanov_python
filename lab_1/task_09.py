ip = input("Введите IP: ")
segments = ip.split(".")

if len(segments) != 4:
    print("Ошибка: IP должен содержать 4 части.")
else:
    a, b, c, d = segments

    if all(seg.isdigit() and 0 <= int(seg) <= 255 for seg in [a, b, c, d]):
        print("IP-адрес корректен.")
    else:
        print("Ошибка: некорректные значения в IP.")