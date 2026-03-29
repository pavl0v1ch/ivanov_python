import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ===== Загрузка данных =====
data = pd.read_excel("sales_data.xlsx", sheet_name="Данные", skiprows=1)
data = data.dropna(axis=1, how="all")
data.columns = ["Дата", "Год", "ГодМесяц", "Точка", "Бренд", "Товар", "Кол-во", "Выручка", "Себестоимость"]

# ===== Добавляем новые показатели =====
data["Цена_ср"] = data["Выручка"] / data["Кол-во"]
data["Маржа"] = data["Выручка"] - data["Себестоимость"]
data["Маржинальность_%"] = (data["Маржа"] / data["Выручка"] * 100).round(1)

# ===== Анализ по точкам реализации =====
points = data.groupby("Точка").agg({
    "Кол-во": "sum",
    "Выручка": ["sum", "mean"],
    "Себестоимость": "sum",
    "Маржа": "sum"
}).round(0)
points.columns = ["Кол-во", "Выручка_сумма", "Выручка_средн", "Себестоимость", "Маржа"]

fig, axs = plt.subplots(2, 2, figsize=(14, 9))
axs[0, 0].bar(points.index, points["Выручка_сумма"], color="steelblue")
axs[0, 0].set_title("Суммарная выручка по точкам")
axs[0, 0].tick_params(axis="x", rotation=45)

axs[0, 1].bar(points.index, points["Выручка_средн"], color="seagreen")
axs[0, 1].set_title("Средняя выручка на точку")
axs[0, 1].tick_params(axis="x", rotation=45)

axs[1, 0].bar(points.index, points["Кол-во"], color="darkorange")
axs[1, 0].set_title("Количество продаж по точкам")
axs[1, 0].tick_params(axis="x", rotation=45)

axs[1, 1].bar(points.index, points["Маржа"], color="purple")
axs[1, 1].set_title("Прибыль по точкам")
axs[1, 1].tick_params(axis="x", rotation=45)

fig.suptitle("Анализ по точкам реализации", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()

# ===== Анализ по товарам =====
products = data.groupby("Товар").agg({
    "Кол-во": "sum",
    "Выручка": "sum",
    "Себестоимость": "sum",
    "Цена_ср": "mean",
    "Маржа": "sum",
    "Маржинальность_%": "mean"
}).round(0)

fig, axs = plt.subplots(2, 2, figsize=(14, 9))
products.nlargest(10, "Выручка")["Выручка"].plot(kind="barh", ax=axs[0, 0], color="navy")
axs[0, 0].set_title("Топ-10 товаров по выручке")

products.nlargest(10, "Маржа")["Маржа"].plot(kind="barh", ax=axs[0, 1], color="darkred")
axs[0, 1].set_title("Топ-10 товаров по прибыли")

products.nlargest(10, "Кол-во")["Кол-во"].plot(kind="barh", ax=axs[1, 0], color="forestgreen")
axs[1, 0].set_title("Топ-10 товаров по количеству")

products.nlargest(10, "Цена_ср")["Цена_ср"].plot(kind="barh", ax=axs[1, 1], color="goldenrod")
axs[1, 1].set_title("Топ-10 товаров по средней цене")

fig.suptitle("Анализ по товарам", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()

# ===== Динамика продаж =====
monthly = data.groupby("ГодМесяц").agg({
    "Кол-во": "sum",
    "Выручка": "sum",
    "Маржа": "sum"
}).reset_index()
monthly["Рост_%"] = monthly["Выручка"].pct_change() * 100

fig, axs = plt.subplots(2, 2, figsize=(14, 9))
axs[0, 0].plot(monthly["ГодМесяц"].astype(str), monthly["Выручка"], marker="o", color="blue")
axs[0, 0].set_title("Динамика выручки")
axs[0, 0].tick_params(axis="x", rotation=45)

axs[0, 1].plot(monthly["ГодМесяц"].astype(str), monthly["Кол-во"], marker="s", color="red")
axs[0, 1].set_title("Динамика количества продаж")
axs[0, 1].tick_params(axis="x", rotation=45)

axs[1, 0].bar(monthly["ГодМесяц"].astype(str), monthly["Рост_%"].fillna(0),
              color=["green" if x >= 0 else "crimson" for x in monthly["Рост_%"].fillna(0)])
axs[1, 0].set_title("Рост/спад продаж (%)")
axs[1, 0].tick_params(axis="x", rotation=45)

axs[1, 1].plot(monthly["ГодМесяц"].astype(str), monthly["Маржа"], marker="^", color="orange")
axs[1, 1].set_title("Динамика прибыли")
axs[1, 1].tick_params(axis="x", rotation=45)

fig.suptitle("Динамика товарооборота", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.show()

# ===== Прогноз по топ-товарам =====
top_goods = products.nlargest(5, "Выручка").index
forecast_list = []

for g in top_goods:
    series = data[data["Товар"] == g].groupby("ГодМесяц")["Кол-во"].sum()
    if len(series) > 2:
        avg_last = series.tail(3).mean()
        trend = series.pct_change().mean()
        forecast_val = avg_last * (1 + (trend if not pd.isna(trend) else 0.05))
        forecast_list.append({"Товар": g, "Средние_продажи": int(avg_last), "Прогноз": int(forecast_val)})

forecast = pd.DataFrame(forecast_list)

if not forecast.empty:
    plt.figure(figsize=(10, 6))
    idx = np.arange(len(forecast))
    plt.bar(idx - 0.2, forecast["Средние_продажи"], width=0.4, label="Факт", color="dodgerblue")
    plt.bar(idx + 0.2, forecast["Прогноз"], width=0.4, label="Прогноз", color="tomato")
    plt.xticks(idx, forecast["Товар"], rotation=45)
    plt.title("Прогноз продаж по топ-товарам")
    plt.ylabel("Количество, шт.")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

# ===== Итоговые показатели =====
print("ИТОГОВЫЕ ПОКАЗАТЕЛИ:")
print(f"Товарооборот: {data['Выручка'].sum():,.0f} руб.")
print(f"Количество продаж: {data['Кол-во'].sum():,.0f} шт.")
print(f"Прибыль: {data['Маржа'].sum():,.0f} руб.")
print(f"Средняя цена: {data['Цена_ср'].mean():.0f} руб.")
print(f"Маржинальность: {data['Маржинальность_%'].mean():.1f}%")
print(f"Товаров: {data['Товар'].nunique()} шт.")
print(f"Точек: {data['Точка'].nunique()} шт.")
print(f"Период: {data['ГодМесяц'].min()} - {data['ГодМесяц'].max()}")

print("\nЛУЧШИЕ ПОКАЗАТЕЛИ:")
print(f"Топ товар: {products.nlargest(1, 'Выручка').index[0]}")
print(f"Топ точка: {points.nlargest(1, 'Выручка_сумма').index[0]}")
