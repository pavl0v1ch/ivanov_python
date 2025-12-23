#структура в которой есть список групп, в ней можно добавлять, удалять и менять студентов
import json

FILENAME = "groups.json"

def load_data():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f" Запуск функции: {func.__name__}")
        result = func(*args, **kwargs)
        print(f" Завершение : {func.__name__}")
        return result
    return wrapper

@log_action
def show_all_groups():
    data = load_data()
    if not data:
        print("Групп нет.")
    else:
        for group, students in data.items():
            print(f"Группа {group}: {students}")

data = load_data()

while True:
    print("\nМеню:")
    print("1. Создать группу")
    print("2. Добавить студента")
    print("3. Удалить студента")
    print("4. Изменить студента")
    print("5. Показать все группы")
    print("6. Сохранить")
    print("0. Выход")

    choice = input("Выберите пункт: ").strip()

    if choice == "0":
        print("Выход.")
        break

    elif choice == "1":
        group_name = input("Название группы: ").strip()
        if group_name in data:
            print("Группа уже существует.")
        else:
            data[group_name] = []
            print("Группа создана.")

    elif choice == "2":
        group_name = input("Название группы: ").strip()
        if group_name not in data:
            print("Группа не найдена.")
        else:
            name = input("Имя и фамилия студента: ").strip()
            if name in data[group_name]:
                print("Студент уже есть в группе.")
            else:
                data[group_name].append(name)
                print("Студент добавлен.")

    elif choice == "3":
        group_name = input("Название группы: ").strip()
        if group_name not in data:
            print("Группа не найдена.")
        else:
            name = input("Имя и фамилия студента: ").strip()
            if name in data[group_name]:
                data[group_name].remove(name)
                print("Студент удалён.")
            else:
                print("Студент не найден.")

    elif choice == "4":
        group_name = input("Название группы: ").strip()
        if group_name not in data:
            print("Группа не найдена.")
        else:
            old_name = input("Текущее имя и фамилия: ").strip()
            if old_name not in data[group_name]:
                print("Студент не найден.")
            else:
                new_name = input("Новые имя и фамилия: ").strip()
                if new_name in data[group_name]:
                    print("Студент с таким именем уже есть.")
                else:
                    data[group_name].remove(old_name)
                    data[group_name].append(new_name)
                    print("Студент изменён.")

    elif choice == "5":
        show_all_groups()

    elif choice == "6":
        save_data(data)
        print("Сохранено в файл.")

    else:
        print("Неверный пункт меню.")