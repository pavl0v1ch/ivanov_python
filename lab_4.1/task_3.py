import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Цвета
gray = '#888888'
beige = '#f5e6c8'
black = '#000000'
white = '#ffffff'

#  ГОЛОВА
head = patches.Ellipse((0, 3), width=4, height=3.5, facecolor=gray)
face = patches.Ellipse((0, 2.7), width=2.5, height=1.8, facecolor=beige)
ax.add_patch(head)
ax.add_patch(face)

# Уши
ax.add_patch(patches.Circle((-2.2, 3.5), 0.6, facecolor=gray))
ax.add_patch(patches.Circle((-2.2, 3.5), 0.4, facecolor=beige))
ax.add_patch(patches.Circle((2.2, 3.5), 0.6, facecolor=gray))
ax.add_patch(patches.Circle((2.2, 3.5), 0.4, facecolor=beige))

# Глаза
ax.add_patch(patches.Circle((-0.6, 3.4), 0.3, facecolor=white))
ax.add_patch(patches.Circle((-0.6, 3.4), 0.1, facecolor=black))
ax.add_patch(patches.Circle((0.6, 3.4), 0.3, facecolor=white))
ax.add_patch(patches.Circle((0.6, 3.4), 0.1, facecolor=black))

# Нос
ax.add_patch(patches.Ellipse((-0.2, 2.9), 0.15, 0.1, facecolor=black))
ax.add_patch(patches.Ellipse((0.2, 2.9), 0.15, 0.1, facecolor=black))

# Рот
ax.add_patch(patches.Arc((0, 2.5), 1.2, 0.6, theta1=200, theta2=340, color=black, linewidth=2))

# ТЕЛО
body = patches.Ellipse((0, -0.5), width=3.5, height=4.5, facecolor=gray)
belly = patches.Ellipse((0, -0.5), width=2.2, height=3.0, facecolor=beige)
ax.add_patch(body)
ax.add_patch(belly)

# Руки
ax.add_patch(patches.Ellipse((-1.6, 0.5), 1.4, 0.5, angle=20, facecolor=gray))
ax.add_patch(patches.Ellipse((1.6, 0.5), 1.4, 0.5, angle=-20, facecolor=gray))

# Ладони
ax.add_patch(patches.Ellipse((-2.4, 0.2), 0.5, 0.3, facecolor=beige))  # левее
ax.add_patch(patches.Ellipse((2.4, 0.2), 0.5, 0.3, facecolor=beige))   # правее

# Ноги
ax.add_patch(patches.Ellipse((-1.0, -3.0), 0.8, 1.2, facecolor=gray))
ax.add_patch(patches.Ellipse((1.0, -3.0), 0.8, 1.2, facecolor=gray))

# Ступни
ax.add_patch(patches.Ellipse((-1.0, -3.7), 0.6, 0.3, facecolor=beige))
ax.add_patch(patches.Ellipse((1.0, -3.7), 0.6, 0.3, facecolor=beige))

plt.xlim(-4, 4)
plt.ylim(-5, 6)
plt.show()
