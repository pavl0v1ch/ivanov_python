def combine_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Возвращает новый словарь, содержащий все пары ключ-значение из dict1 и dict2.
    Если ключ повторяется, используется значение из dict2.
    """
    return {**dict1, **dict2}

