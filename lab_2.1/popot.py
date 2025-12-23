
import json

rooms = {}

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f" Запуск функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f" Завершение функции: {func.__name__}")
        return result
    return wrapper

@log_action
def save_to_file():
    with open("rooms.json", "w", encoding="utf-8") as f:
        json.dump(rooms, f, ensure_ascii=False, indent=2)
    print("Сохранено в rooms.json")



while True:
    print("\nМеню:")
    print("1. Показать список")
    print("2. Добавить кабинет")
    print("3. Изменить кабинет")
    print("4. Удалить кабинет")
    print("5. Сохранить в файл")
    print("0. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        if not rooms:
            print("Список пуст.")
        else:
            for name, seats in rooms.items():
                print(f"{name}: {seats} мест")

    elif choice == "2":
        name = input("Название кабинета: ")
        try:
            seats = int(input("Количество мест: "))
            if seats <= 0:
                print("Количество мест должно быть положительным числом.")
            else:
                rooms[name] = seats
                print("Добавлено.")
        except ValueError:
            print("Ошибка: введите целое число.")

    elif choice == "3":
        name = input("Название кабинета для изменения: ")
        if name in rooms:
            try:
                seats = int(input("Новое количество мест: "))
                if seats <= 0:
                    print("Количество мест должно быть положительным числом.")
                else:
                    rooms[name] = seats
                    print("Изменено.")
            except ValueError:
                print("Ошибка: введите целое число.")
        else:
            print("Такого кабинета нет.")

    elif choice == "4":
        name = input("Название кабинета для удаления: ")
        if name in rooms:
            del rooms[name]
            print("Удалено.")
        else:
            print("Такого кабинета нет.")

    elif choice == "5":
        save_to_file()

    elif choice == "0":
        print("Выход.")
        break

    else:
        print("Неверный пункт меню.")