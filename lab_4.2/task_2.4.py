import numpy as np
from scipy.integrate import quad, dblquad

# Определённый интеграл: ∫₀^π sin(x) dx
def f1(x):
    return np.sin(x)

result1, _ = quad(f1, 0, np.pi)

# Двойной интеграл: ∫₀¹ ∫₀¹ (x² + y²) dy dx
def f2(y, x):
    return x**2 + y**2

result2, _ = dblquad(f2, 0, 1, lambda x: 0, lambda x: 1)


print(f"Определённый интеграл ∫₀^π sin(x) dx = {round(result1, 3)}")
print(f"Двойной интеграл ∫₀¹ ∫₀¹ (x² + y²) dy dx = {round(result2, 3)}")
