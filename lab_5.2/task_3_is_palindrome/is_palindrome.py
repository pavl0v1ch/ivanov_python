def is_palindrome(value) -> bool:
    """
    Проверяет, является ли строка или число палиндромом.
    Возвращает True, если палиндром, иначе False.
    """
    text = str(value).lower()
    return text == text[::-1]
