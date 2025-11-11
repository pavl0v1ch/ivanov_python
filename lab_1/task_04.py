amount = input("Сумма в рублях (целое число): ")

if not amount.isdigit():
    print("Ошибка: введите корректное целое число.")
else:
    amount = int(amount)

    bills_100 = amount // 100
    amount %= 100

    bills_50 = amount // 50
    amount %= 50

    bills_10 = amount // 10
    amount %= 10

    bills_5 = amount // 5
    amount %= 5

    bills_2 = amount // 2
    amount %= 2

    bills_1 = amount

    print(f"100 руб.: {bills_100}")
    print(f"50 руб.: {bills_50}")
    print(f"10 руб.: {bills_10}")
    print(f"5 руб.: {bills_5}")
    print(f"2 руб.: {bills_2}")
    print(f"1 руб.: {bills_1}")