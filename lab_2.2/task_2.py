# Определяется функция merge_dicts, которая принимает два словаря: d1 и d2.
# Цель функции — объединить содержимое второго словаря d2 в первый словарь d1.
# При совпадении ключей происходит замена значений или рекурсивное слияние вложенных словарей.
def merge_dicts(d1, d2):
    for key in d2:

        # Если ключ из d2 уже существует в d1:
        if key in d1:

            # Проверяется, являются ли значения по этому ключу словарями.
            # Если оба значения словари, вызывается рекурсивное слияние.
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                merge_dicts(d1[key], d2[key])
            elif isinstance(d1[key], list) and isinstance(d2[key], list):
                merge_dicts(d1[key], d2[key])
            elif isinstance(d1[key], set) and isinstance(d2[key], set):
                merge_dicts(d1[key], d2[key])
            elif isinstance(d1[key], tuple) and isinstance(d2[key], tuple):
                merge_dicts(d1[key], d2[key])


            # Если хотя бы одно значение не является словарём — значение из d2 заменяет значение в d1.
            else:
                d1[key] = d2[key]

        # Если ключ отсутствует в d1 — он просто добавляется со значением из d2.
        else:
            d1[key] = d2[key]



if __name__ == "__main__":
    # Создаются два словаря с вложенными структурами.
    dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
    dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

    # Вызывается функция merge_dicts для объединения dict_b в dict_a.
    # Вложенные словари также объединяются рекурсивно.
    merge_dicts(dict_a, dict_b)


    print(f"Результат слияния: {dict_a}")
