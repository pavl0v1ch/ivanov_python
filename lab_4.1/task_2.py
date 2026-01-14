import numpy as np
import matplotlib.pyplot as plt

# Интервал с исключением точек x = ±3 (асимптоты)
x = np.linspace(-10, 10, 1000)
x = x[np.abs(x - 3) > 0.05]  # исключаем окрестность x = 3
x = x[np.abs(x + 3) > 0.05]  # исключаем окрестность x = -3

# Вычисление функции
f_x = 5 / (x**2 - 9)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label='f(x) = 5 / (x² - 9)', color='purple')

# Вертикальные асимптоты
plt.axvline(x=3, color='gray', linestyle='--', label='Асимптота x = 3')
plt.axvline(x=-3, color='gray', linestyle='--', label='Асимптота x = -3')

# Оформление
plt.title('График функции f(x) = 5 / (x² - 9)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
