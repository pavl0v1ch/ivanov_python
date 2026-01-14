import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

# Средний балл ЦЭ/ЦТ по предметам
subjects = ["Математика", "Физика", "Химия", "История", "Обществознание"]
for subject in subjects:
    sns.lineplot(data=df, x="Год", y=subject, label=subject, ci=None)

plt.title("Средний балл ЦЭ/ЦТ по предметам")
plt.legend()
plt.show()

# Динамика среднего балла при поступлении
sns.lineplot(data=df, x="Год", y="Средний балл при поступлении", ci=None)
plt.title("Динамика среднего балла при поступлении")
plt.show()

# Количество поступивших по специальностям
sns.countplot(data=df, x="Специальность", order=df["Специальность"].value_counts().index)
plt.title("Количество поступивших по специальностям")
plt.xticks(rotation=45)
plt.show()

# Статистика по формам обучения
sns.countplot(data=df, x="Форма обучения", order=df["Форма обучения"].value_counts().index)
plt.title("Статистика по формам обучения")
plt.show()
