class EmployeeAlreadyExists(Exception):
    pass


class EmployeeNotFound(Exception):
    pass


class NotAtWorkError(Exception):
    pass


class NoTasksCompletedError(Exception):
    pass


class Employee:
    def __init__(self, name, position, experience, emp_id, base_salary=1000):
        self.name = name
        self.position = position
        self.experience = int(experience)
        self.emp_id = emp_id
        self.at_work = False
        self.base_salary = base_salary
        self.tasks_done = 0

    def come_to_work(self):
        if self.at_work:
            print(f"{self.name} уже на работе.")
        else:
            self.at_work = True
            print(f"{self.name} пришёл на работу.")

    def leave_work(self):
        if not self.at_work:
            NotAtWorkError(f"{self.name} не может уйти — он ещё не пришёл.")

        else:
            print(f"{self.name} ушёл с работы.")
        self.at_work = False

    def do_task(self):
        if self.at_work:
            self.tasks_done += 1
            print(f"{self.name} выполняет задачу ({self.position}). Всего выполнено: {self.tasks_done}")
        else:
            print(f"{self.name} не на работе, задачи не выполняются.")

    def calculate_salary(self):
        return self.base_salary + (self.experience * 200) + (self.tasks_done * 50)

    def get_salary(self):
        if self.tasks_done == 0:
            raise NoTasksCompletedError(f"{self.name} не может получить зарплату — задачи не выполнены.")
        salary = self.calculate_salary()
        print(f"{self.name} получит зарплату в следующем месяце: {salary} BYN")
        self.tasks_done = 0


class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, position, experience, emp_id):
        if emp_id in self.employees:
            raise EmployeeAlreadyExists("Сотрудник с таким ID уже существует.")
        self.employees[emp_id] = Employee(name, position, experience, emp_id)

    def get_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFound("Сотрудник не найден.")
        return self.employees[emp_id]


def main():
    manager = EmployeeManager()

    while True:
        print("\nГлавное меню:")
        print("1. Добавить сотрудника")
        print("2. Войти как сотрудник")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            position = input("Должность: ").strip()
            experience = input("Стаж (лет): ").strip()
            emp_id = input("ID сотрудника: ").strip()
            try:
                manager.add_employee(name, position, experience, emp_id)
                print("Сотрудник добавлен.")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            emp_id = input("Введите ID: ").strip()
            try:
                emp = manager.get_employee(emp_id)
                print(f"\nВход: {emp.name}, должность: {emp.position}")
            except Exception as e:
                print(f"Ошибка: {e}")
                continue

            while True:
                print("\nМеню сотрудника:")
                print("1. Прийти на работу")
                print("2. Уйти с работы")
                print("3. Выполнять задачи")
                print("4. Получить зарплату")
                print("0. Выйти в главное меню")
                cmd = input("Выберите действие: ").strip()

                try:
                    if cmd == "1":
                        emp.come_to_work()
                    elif cmd == "2":
                        emp.leave_work()
                    elif cmd == "3":
                        emp.do_task()
                    elif cmd == "4":
                        emp.get_salary()
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
            print("Неверный ввод.")


if __name__ == "__main__":
    main()


    class EmployeeAlreadyExists(Exception):
        pass


    class EmployeeNotFound(Exception):
        pass


    class NotAtWorkError(Exception):
        pass


    class NoTasksCompletedError(Exception):
        pass


    class Employee:
        def init(self, name, position, experience, emp_id, base_salary=1000):
            self.name = name
            self.position = position
            self.experience = int(experience)
            self.emp_id = emp_id
            self.at_work = False
            self.base_salary = base_salary
            self.tasks_done = 0

        def come_to_work(self):
            if self.at_work:
                print(f"{self.name} уже на работе.")
            else:
                self.at_work = True
                print(f"{self.name} пришёл на работу.")

        def leave_work(self):
            if not self.at_work:
                raise NotAtWorkError(f"{self.name} не может уйти — он ещё не пришёл.")
            else:
                self.at_work = False
                print(f"{self.name} ушёл с работы.")

        def do_task(self):
            if self.at_work:
                self.tasks_done += 1
                print(f"{self.name} выполняет задачу ({self.position}). Всего выполнено: {self.tasks_done}")
            else:
                print(f"{self.name} не на работе, задачи не выполняются.")

        def calculate_salary(self):
            return self.base_salary + (self.experience * 200) + (self.tasks_done * 50)

        def get_salary(self):
            if self.tasks_done == 0:
                raise NoTasksCompletedError(f"{self.name} не может получить зарплату — задачи не выполнены.")
            salary = self.calculate_salary()
            print(f"{self.name} получит зарплату в следующем месяце: {salary} BYN")
            self.tasks_done = 0


    class EmployeeManager:
        def init(self):
            self.employees = {}

        def add_employee(self, name, position, experience, emp_id):
            try:
                if emp_id in self.employees:
                    raise EmployeeAlreadyExists("Сотрудник с таким ID уже существует.")
                self.employees[emp_id] = Employee(name, position, experience, emp_id)

            except EmployeeAlreadyExists as e:
                print(f"Ошибка: {e}")
            else:
                print(f"Сотрудник {name} успешно добавлен (ID: {emp_id}).")
            finally:
                print("Операция добавления завершена.")

        def get_employee(self, emp_id):
            if emp_id not in self.employees:
                raise EmployeeNotFound(f"Сотрудник с ID {emp_id} не найден.")
            return self.employees[emp_id]


    def main():
        manager = EmployeeManager()

        while True:
            print("\nГлавное меню:")
            print("1. Добавить сотрудника")
            print("2. Войти как сотрудник")
            print("0. Выход")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                name = input("Имя: ").strip()
                position = input("Должность: ").strip()
                experience = input("Стаж (лет): ").strip()
                emp_id = input("ID сотрудника: ").strip()
                try:
                    manager.add_employee(name, position, experience, emp_id)
                except Exception as e:
                    print(f"Ошибка: {e}")

            elif choice == "2":
                emp_id = input("Введите ID: ").strip()
                try:
                    emp = manager.get_employee(emp_id)
                    print(f"\nВход: {emp.name}, должность: {emp.position}")
                except Exception as e:
                    print(f"Ошибка: {e}")
                    continue

                while True:
                    print("\nМеню сотрудника:")
                    print("1. Прийти на работу")
                    print("2. Уйти с работы")
                    print("3. Выполнять задачи")
                    print("4. Получить зарплату")
                    print("0. Выйти в главное меню")
                    cmd = input("Выберите действие: ").strip()

                    try:
                        if cmd == "1":
                            emp.come_to_work()
                        elif cmd == "2":
                            emp.leave_work()
                        elif cmd == "3":
                            emp.do_task()
                        elif cmd == "4":
                            emp.get_salary()
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
                print("Неверный ввод.")


    if __name__ == "__main__":
        main()



