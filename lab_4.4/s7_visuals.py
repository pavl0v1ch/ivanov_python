import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


df = pd.read_excel("s7_data_sample_rev4_50k.xlsx", sheet_name="DATA", parse_dates=["ISSUE_DATE"])

# Временные признаки
df["Month"] = df["ISSUE_DATE"].dt.month
df["Weekday"] = df["ISSUE_DATE"].dt.day_name()
df["Hour"] = df["ISSUE_DATE"].dt.hour

#  График продажи по месяцам
sns.countplot(data=df, x="Month", palette="Blues")
plt.title("Количество продаж по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Количество билетов")
plt.tight_layout()
plt.show()

#  График продажи по дням недели
order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sns.countplot(data=df, x="Weekday", order=order, palette="Greens")
plt.title("Количество продаж по дням недели")
plt.xlabel("День недели")
plt.ylabel("Количество билетов")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  График продажи по часам
sns.histplot(data=df, x="Hour", bins=24, kde=False, color="orange")
plt.title("Количество продаж по часам")
plt.xlabel("Час дня")
plt.ylabel("Количество билетов")
plt.tight_layout()
plt.show()

#  График способы оплаты
payment_map = {
    "AH": "Инвойс", "AX": "Инвойс", "BA": "Банковская карта", "CN": "Наличные",
    "CX": "Динамическое ценообразование", "VA": "Ваучер", "VD": "Ваучер"
}
df["PaymentMethod"] = df["FOP_TYPE_CODE"].map(payment_map).fillna("Другое")
sns.countplot(data=df, x="PaymentMethod", palette="Purples")
plt.title("Способы оплаты")
plt.xlabel("Метод")
plt.ylabel("Количество билетов")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# График типы пассажиров
pax_map = {"AD": "Взрослый", "CH": "Ребёнок", "IN": "Младенец", "FM": "Семья"}
df["PassengerType"] = df["PAX_TYPE"].map(pax_map).fillna("Неизвестно")
sns.countplot(data=df, x="PassengerType", palette="Reds")
plt.title("Типы пассажиров")
plt.xlabel("Тип")
plt.ylabel("Количество билетов")
plt.tight_layout()
plt.show()

# График тип маршрута
route_map = {"ВВП": "Внутренний", "МВП": "Международный", "FFP": "Лояльность"}
df["RouteType"] = df["ROUTE_FLIGHT_TYPE"].map(route_map).fillna("Другое")
sns.countplot(data=df, x="RouteType", palette="coolwarm")
plt.title("Типы маршрутов")
plt.xlabel("Маршрут")
plt.ylabel("Количество билетов")
plt.tight_layout()
plt.show()

#График тип продажи
sns.countplot(data=df, x="SALE_TYPE", palette="gray")
plt.title("Типы продаж")
plt.xlabel("Тип")
plt.ylabel("Количество билетов")
plt.tight_layout()
plt.show()
