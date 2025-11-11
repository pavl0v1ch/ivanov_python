pressure = float(input("Введите давление в Паскалях: "))
volume = float(input("Введите объем в кубических метрах: "))
temperature = float(input("Введите температуру в Кельвинах: "))

R = 8.314  # универсальная газовая постоянная
moles = (pressure * volume) / (R * temperature)

print("Рассчитанное количество молей:", moles)