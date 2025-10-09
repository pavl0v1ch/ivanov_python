import json
from datetime import datetime

# Исключения — для контроля ошибок
class ClientAlreadyExists(Exception): pass
class AccountAlreadyExists(Exception): pass
class AccountNotFound(Exception): pass
class InsufficientFunds(Exception): pass
class CurrencyMismatch(Exception): pass
class ClientNotFound(Exception): pass

# Класс банковского счёта
class Account:
    def __init__(self, currency, balance=0):
        self.currency = currency
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнено: {amount} {self.currency}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Недостаточно средств.")
        self.balance -= amount
        print(f"Снято: {amount} {self.currency}")

# Класс клиента
class Client:
    def __init__(self, name, surname, client_id):
        self.name = name
        self.surname = surname
        self.client_id = client_id
        self.accounts = {}  # ключ — валюта, значение — объект Account

    def open_account(self, currency):
        if currency in self.accounts:
            raise AccountAlreadyExists("Счёт уже существует.")
        self.accounts[currency] = Account(currency)

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт не найден.")
        del self.accounts[currency]

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFound("Счёт не найден.")
        return self.accounts[currency]

    def get_summary(self):
        summary = {cur: acc.balance for cur, acc in self.accounts.items()}
        total = sum(summary.values())
        return summary, total

# Класс банка
class Bank:
    def __init__(self):
        self.clients = {}  # client_id → объект Client

    def create_client(self, name, surname, client_id):
        if client_id in self.clients:
            raise ClientAlreadyExists("Клиент уже существует.")
        self.clients[client_id] = Client(name, surname, client_id)

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ClientNotFound("Клиент не найден.")
        return self.clients[client_id]

    def transfer(self, from_id, currency, to_id, to_currency, amount):
        sender = self.get_client(from_id)
        receiver = self.get_client(to_id)

        if currency != to_currency:
            raise CurrencyMismatch("Нельзя переводить между разными валютами.")

        sender_acc = sender.get_account(currency)
        receiver_acc = receiver.get_account(currency)

        sender_acc.withdraw(amount)
        receiver_acc.deposit(amount)
        print(f"Переведено {amount} {currency} от {from_id} к {to_id}")

    def export_summary(self, client_id):
        client = self.get_client(client_id)
        summary, total = client.get_summary()
        data = {
            "Клиент": f"{client.surname} {client.name}",
            "ID": client.client_id,
            "Счета": summary,
            "Суммарный баланс": total,
            "Время": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(f"summary_{client_id}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Выписка сохранена.")

# Интерфейс
def main():
    bank = Bank()
    print("=" * 50)
    print("  Добро пожаловать в банковскую систему")
    print("=" * 50)

    while True:
        print("\nГлавное меню:")
        print("-" * 50)
        print("1. Зарегистрировать клиента")
        print("2. Войти в систему")
        print("0. Выход")
        print("-" * 50)
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            surname = input("Фамилия: ").strip()
            client_id = input("ID клиента: ").strip()
            try:
                bank.create_client(name, surname, client_id)
                print("Клиент зарегистрирован.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            client_id = input("Введите ваш ID: ").strip()
            try:
                client = bank.get_client(client_id)
                print(f"\n Вход: {client.name} {client.surname}")
                print(f"Время входа: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            except Exception as e:
                print(f"⚠Ошибка: {e}")
                continue

            while True:
                print("\nМеню клиента:")
                print("-" * 50)
                print("1. Открыть счёт")
                print("2. Закрыть счёт")
                print("3. Пополнить счёт")
                print("4. Снять деньги")
                print("5. Перевести деньги")
                print("6. Сохранить выписку")
                print("0. Выйти в главное меню")
                print("-" * 50)
                cmd = input("Выберите действие: ").strip()

                try:
                    if cmd == "1":
                        currency = input("Валюта: ").strip()
                        client.open_account(currency)
                        print("Счёт открыт.")

                    elif cmd == "2":
                        currency = input("Валюта: ").strip()
                        client.close_account(currency)
                        print("Счёт закрыт.")

                    elif cmd == "3":
                        currency = input("Валюта: ").strip()
                        amount = float(input("Сумма: "))
                        client.get_account(currency).deposit(amount)

                    elif cmd == "4":
                        currency = input("Валюта: ").strip()
                        amount = float(input("Сумма: "))
                        client.get_account(currency).withdraw(amount)

                    elif cmd == "5":
                        to_id = input("ID получателя: ").strip()
                        currency = input("Валюта: ").strip()
                        amount = float(input("Сумма: "))
                        if to_id != client_id:
                            print("Можно переводить только между своими счетами.")
                            continue
                        bank.transfer(client_id, currency, to_id, currency, amount)

                    elif cmd == "6":
                        bank.export_summary(client_id)

                    elif cmd == "0":
                        print("Возврат в главное меню.")
                        break

                    else:
                        print("Неверный выбор.")

                except Exception as e:
                    print(f"Ошибка: {e}")

        elif choice == "0":
            print("Завершение работы.")
            break

        else:
            print(" Неверный ввод.")

if __name__ == "__main__":
    main()
