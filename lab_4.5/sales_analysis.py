import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import numpy as np

# Загрузка данных
def detect_header_row(path, sheet):
    for i in range(10):
        df_try = pd.read_excel(path, sheet_name=sheet, skiprows=i, nrows=1)
        if any("Дата" in col for col in df_try.columns):
            return i
    raise ValueError("Не удалось найти строку с заголовками")

file_path = "sales_data.xlsx"
sheet_name = "Данные"
header_row = detect_header_row(file_path, sheet_name)
df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=header_row)

#  Предобработка
df["Дата"] = pd.to_datetime(df["Дата"], errors="coerce")
df = df.dropna(subset=["Дата", "точка", "товар", "Продажи", "Количество", "Себестоимость"])
df["Средняя цена"] = df["Продажи"] / df["Количество"]

#  Группировка по точкам и товарам
grouped = df.groupby(["точка", "товар"]).agg({
    "Продажи": "sum",
    "Количество": "sum",
    "Себестоимость": "sum",
    "Средняя цена": "mean"
}).reset_index()

# Общий товарооборот
total_turnover = df["Продажи"].sum()
print(f"\n📦 Общий товарооборот: {total_turnover:,.0f} руб.")

#  Визуализация: продажи по точкам
plt.figure(figsize=(10, 6))
point_sales = df.groupby("точка")["Продажи"].sum().sort_values(ascending=False)
sns.barplot(x=point_sales.index, y=point_sales.values)
plt.title("Общие продажи по точкам")
plt.ylabel("Сумма продаж")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Визуализация: динамика продаж по товарам
plt.figure(figsize=(12, 6))
df_monthly = df.groupby([df["Дата"].dt.to_period("M"), "товар"])["Продажи"].sum().unstack().fillna(0)
df_monthly.index = df_monthly.index.to_timestamp()
df_monthly.plot(figsize=(12, 6))
plt.title("Динамика продаж по товарам")
plt.ylabel("Сумма продаж")
plt.xlabel("Месяц")
plt.tight_layout()
plt.show()

#  Прогноз продаж по каждому товару
print("\nПрогноз продаж по каждому товару:")
for product in df["товар"].unique():
    df_prod = df[df["товар"] == product].copy()
    df_prod["Месяц"] = df_prod["Дата"].dt.to_period("M").astype(str)
    monthly_sales = df_prod.groupby("Месяц")["Продажи"].sum().reset_index()
    monthly_sales["Месяц_номер"] = np.arange(len(monthly_sales))

    if len(monthly_sales) >= 3:
        model = LinearRegression()
        model.fit(monthly_sales[["Месяц_номер"]], monthly_sales["Продажи"])
        next_month = len(monthly_sales)
        forecast = model.predict([[next_month]])
        print(f"- {product}: прогноз на следующий месяц ≈ {forecast[0]:,.0f} руб.")
