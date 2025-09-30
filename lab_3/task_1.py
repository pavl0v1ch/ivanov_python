class BankError(Exception):
    """Общая ошибка банка."""
    pass


class CurrencyError(BankError):
    """Ошибка: валюты счетов не совпадают."""
    pass


class FundsError(BankError):
    """Ошибка: недостаточно средств для операции."""
    pass


class AccountError(BankError):
    """Ошибка: проблемы с банковским счётом."""
    pass


class ClientError(BankError):
    """Ошибка: проблемы с клиентом банка."""
    pass


class Bank:
    def __init__(self, clients=None):
        self.clients = clients or [] #инициализация списка клиентов

    def get_client_ids(self):
        return [c.client_id for c in self.clients] # возвращает список всех ID

    def find_client(self, client_id):
        for c in self.clients: # поиск клиента по ID среди зарегистрированных
            if c.client_id == client_id:
                return c
        raise ClientError(f"Клиент с ID {client_id} не найден.")

    def execute_transfer(self, sender_id, sender_currency, receiver_id, receiver_currency, amount):
        sender = self.find_client(sender_id) # получение объекта отправителя и получателя
        receiver = self.find_client(receiver_id)

        sender_acc = sender.get_account(sender_currency) # получаем счета
        receiver_acc = receiver.get_account(receiver_currency)


        if sender_acc.currency != receiver_acc.currency: # проверка валюты
            raise CurrencyError("Нельзя перевести между счетами с разными валютами.")


        sender_acc.withdraw(amount) # -бабки
        receiver_acc.deposit(amount) # +бабки
