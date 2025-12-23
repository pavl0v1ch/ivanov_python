import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Загрузка данных
df = pd.read_csv("students.csv")

df["Общий балл"] = (
    df[["Математика", "Физика", "Химия", "История", "Обществознание"]].clip(upper=50).sum(axis=1) +
    df["Средний балл аттестата"] * 5
)

#Динамика среднего балла ЦЭ/ЦТ по предметам
subjects = ["Математика", "Физика", "Химия", "История", "Обществознание"]
plt.figure(figsize=(10, 6))
for subj in subjects:
    sns.lineplot(data=df, x="Год", y=subj, label=subj, errorbar=None)
plt.title("Средние баллы ЦЭ/ЦТ по предметам")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

#Динамика среднего балла аттестата
avg_att = df.groupby("Год")["Средний балл аттестата"].mean()
plt.figure(figsize=(9, 5))
plt.bar(avg_att.index, avg_att.values, color="forestgreen")
plt.title("Средний балл аттестата по годам")
plt.xlabel("Год поступления")
plt.ylabel("Средний балл")
plt.tight_layout()
plt.show()

#Минимальный проходной балл по специальностям
min_scores = df.groupby(["Год", "Специальность"])["Общий балл"].min().unstack()
plt.figure(figsize=(10, 5))
for spec in min_scores.columns:
    plt.plot(min_scores.index, min_scores[spec], marker="o", label=spec)
plt.title("Минимальный проходной балл по специальностям")
plt.xlabel("Год поступления")
plt.ylabel("Минимальный балл")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

#Количество студентов по специальностям
spec_counts = df["Специальность"].value_counts()
plt.figure(figsize=(8, 4))
plt.bar(spec_counts.index, spec_counts.values, color=["navy", "darkred", "darkorange"])
plt.title("Количество студентов по специальностям")
plt.ylabel("Количество")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

#Статистика по формам обучения с уникальными цветами
form_counts = df["Форма обучения"].value_counts()
form_colors = {
    "Очная": "lightcoral", "Заочная": "skyblue", "Вечерняя": "gold"
}
color_list = [form_colors.get(label, "gray") for label in form_counts.index]

plt.figure(figsize=(6, 6))
plt.pie(form_counts.values, labels=form_counts.index, autopct="%1.1f%%", startangle=90, colors=color_list)
plt.title("Распределение форм обучения")
plt.tight_layout()
plt.show()

#Итоговые показатели
print("\nИТОГОВЫЕ ПОКАЗАТЕЛИ:")
print(f"Всего студентов: {len(df)}")
print(f"Средний общий балл: {df['Общий балл'].mean():.1f}")
print(f"Максимальный общий балл: {df['Общий балл'].max():.1f}")
print(f"Минимальный общий балл: {df['Общий балл'].min():.1f}")
