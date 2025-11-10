import pandas as pd

# Загружаем Excel с указанием листа
df = pd.read_excel("s7_data_sample_rev4_50k.xlsx", sheet_name="DATA", parse_dates=["ISSUE_DATE", "FLIGHT_DATE_LOC"])

# Временные признаки
df["Month"] = df["ISSUE_DATE"].dt.month
df["Weekday"] = df["ISSUE_DATE"].dt.day_name()
df["Hour"] = df["ISSUE_DATE"].dt.hour

# Способ оплаты
payment_map = {
    "AH": "Инвойс", "AX": "Инвойс", "BA": "Банковская карта", "CN": "Наличные",
    "CX": "Динамическое ценообразование", "VA": "Ваучер", "VD": "Ваучер"
}
df["PaymentMethod"] = df["FOP_TYPE_CODE"].map(payment_map).fillna("Другое")

# Тип пассажира
pax_map = {"AD": "Взрослый", "CH": "Ребёнок", "IN": "Младенец", "FM": "Семья"}
df["PassengerType"] = df["PAX_TYPE"].map(pax_map).fillna("Неизвестно")

# Тип маршрута
route_map = {"ВВП": "Внутренний", "МВП": "Международный", "FFP": "Лояльность"}
df["RouteType"] = df["ROUTE_FLIGHT_TYPE"].map(route_map).fillna("Другое")

# Доход
df["Revenue"] = df["REVENUE_AMOUNT"]

# Агрегации
monthly = df.groupby("Month")["Revenue"].sum()
weekday = df.groupby("Weekday")["Revenue"].sum()
hourly = df.groupby("Hour")["Revenue"].sum()
by_payment = df.groupby("PaymentMethod")["Revenue"].sum()
by_passenger = df.groupby("PassengerType")["Revenue"].sum()
by_route = df.groupby("RouteType")["Revenue"].sum()
by_sale_type = df.groupby("SALE_TYPE")["Revenue"].sum()

# Сохранение результатов
monthly.to_csv("monthly_sales.csv")
weekday.to_csv("weekday_sales.csv")
hourly.to_csv("hourly_sales.csv")
by_payment.to_csv("payment_sales.csv")
by_passenger.to_csv("passenger_sales.csv")
by_route.to_csv("route_sales.csv")
by_sale_type.to_csv("sale_type_sales.csv")

print("Анализ завершён.")
