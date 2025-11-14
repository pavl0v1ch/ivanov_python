import numpy as np
import matplotlib.pyplot as plt

# Интервал в градусах
x_deg = np.linspace(-360, 360, 1000)
x_rad = np.deg2rad(x_deg)

# Функции
f_x = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad)**2 + 1) * np.sin(x_rad)
h_x = -np.log((np.cos(x_rad) + np.sin(x_rad))**2 + 2.5) + 10


plt.figure(figsize=(10, 6))
plt.plot(x_deg, f_x, label='f(x)', color='black')
plt.plot(x_deg, h_x, label='h(x)', color='red')
plt.title('Графики функций f(x) и h(x) на интервале от -360° до 360°')
plt.xlabel('x (градусы)')
plt.ylabel('Значение функции')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
