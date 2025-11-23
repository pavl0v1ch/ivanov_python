def find_unique(lst: list) -> list:
    """
    Возвращает список элементов, которые встречаются в исходном списке только один раз.
    Порядок сохранён.
    """
    return [x for x in lst if lst.count(x) == 1]
