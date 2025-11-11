base_minutes = 60
base_sms = 30
base_mb = 1024
base_price = 24.99


price_minute = 0.59
price_sms = 0.59
price_mb = 0.76
tax_rate = 0.02


used_minutes = int(input("Минуты использовано: "))
used_sms = int(input("SMS отправлено: "))
used_mb = int(input("Интернет-трафик (в МБ): "))


extra_minutes = max(0, used_minutes - base_minutes)
extra_sms = max(0, used_sms - base_sms)
extra_mb = max(0, used_mb - base_mb)


cost_minutes = extra_minutes * price_minute
cost_sms = extra_sms * price_sms
cost_mb = extra_mb * price_mb


subtotal = base_price + cost_minutes + cost_sms + cost_mb
tax = subtotal * tax_rate
total = subtotal + tax


print("\n Счёт за месяц:")
print(f"Базовый тариф: {base_price:.2f} руб.")

if extra_minutes:
    print(f"Доп. минуты: {extra_minutes} мин → {cost_minutes:.2f} руб.")
if extra_sms:
    print(f"Доп. SMS: {extra_sms} шт → {cost_sms:.2f} руб.")
if extra_mb:
    print(f"Доп. интернет: {extra_mb} МБ → {cost_mb:.2f} руб.")

print(f"Налог (2%): {tax:.2f} руб.")
print(f"Итог к оплате: {total:.2f} руб.")