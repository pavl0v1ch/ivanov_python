def are_anagrams(word1: str, word2: str) -> bool:
    """
    Проверяет, являются ли две строки анаграммами.
    Возвращает True, если строки содержат одинаковые буквы в разном порядке.
    """
    return sorted(word1.lower()) == sorted(word2.lower())
