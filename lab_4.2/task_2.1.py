import numpy as np
from scipy import stats

# Расходы на проезд по месяцам (в условных единицах)
expenses = np.array([120, 135, 110, 90, 100, 95, 80, 85, 105, 130, 140, 150])

# Месяцы: 1–12
months = np.arange(1, 13)

# Зимний период: декабрь, январь, февраль
winter_months = [12, 1, 2]
winter_expenses = expenses[[m - 1 for m in winter_months]]
winter_total = np.sum(winter_expenses)

# Летний период: июнь, июль, август
summer_months = [6, 7, 8]
summer_expenses = expenses[[m - 1 for m in summer_months]]
summer_total = np.sum(summer_expenses)

# Сравнение
if winter_total > summer_total:
    print("Зимой тратится больше денег на проезд.")
elif summer_total > winter_total:
    print("Летом тратится больше денег на проезд.")
else:
    print("Зимой и летом расходы на проезд одинаковы.")

# Поиск месяцев с максимальными расходами
max_value = np.max(expenses)
max_months = months[expenses == max_value]

print("Месяцы с наибольшими расходами:", max_months.tolist())
