import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker("ru_RU")
np.random.seed(42)

years = [2021, 2022, 2023, 2024, 2025]
specialties = ["Физика", "Математика", "Химия", "История Беларуси", "Биология"]
subjects = ["Математика", "Физика", "Химия", "История", "Обществознание"]
forms = ["Очная", "Заочная", "Вечерняя"]

def generate_student():
    year = random.choice(years)
    specialty = random.choice(specialties)
    scores = {subject: np.random.randint(40, 100) for subject in subjects}
    avg_exam = round(np.mean(list(scores.values())), 1)
    avg_certificate = round(np.random.uniform(6.0, 10.0), 1)
    avg_total = round((avg_exam + avg_certificate) / 2, 1)
    return {
        "ФИО": fake.name(),
        "Год": year,
        "Специальность": specialty,
        "Средний балл ЦЭ/ЦТ": avg_exam,
        "Средний балл аттестата": avg_certificate,
        "Средний балл при поступлении": avg_total,
        "Адрес": fake.address().replace("\n", ", "),
        "Телефон": fake.phone_number(),
        "Форма обучения": random.choice(forms),
        **scores
    }

data = pd.DataFrame([generate_student() for _ in range(500)])
data.to_csv("students.csv", index=False)
