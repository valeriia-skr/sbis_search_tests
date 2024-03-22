import pytest

from main import search_employees


def test_search_trigger_first_char():
    """"Проверяем, что поиск срабатывает с первого символа."""
    assert search_employees('А') is not None


def test_search_automatic_trigger_third_char():
    """"Проверяем, что поиск автоматически срабатывает с третьего символа."""
    # Предполагаем, что функция возвращает None, если условия поиска не выполнены
    assert search_employees('АБ') is None
    assert search_employees('АБВ') is not None


@pytest.mark.parametrize("query", [
    ("АБВгде123"),
    ("abcDEF456"),
    ("789"),
    ("абвГДЕ"),
    ("XYZxyz")
])
def test_search_allowed_character(query):
    """Проверяем, что поиск работает с разрешенными кириллическими и английскими символами, а также с цифрами."""
    assert search_employees(query) is not None


@pytest.mark.parametrize("query"[
    ("!@#$%"),
    ("абв<>?"),
    ("123_+=-")
])
def test_search_disallowed_characters(query):
    """Проверяем, что поиск не возвращает результаты для недопустимых симоволов."""
    # Этот тест зависит от того, как система должна реагировать на недопустимые символы
    # Например, предположим, что система возвращает пустой список или None
    assert search_employees(query) is None or search_employees(query) == []


# Тест для проверки, что поиск не чувствителен к регистру (если это требуется)
@pytest.mark.parametrize("query, expected"[
    ("абв", True),
    ("АБВ", True),
    ("Abc", True),
    ("ABC", True)
])
def test_search_case_insensitivity(query, expected):
    """Проверяем, что поиск не чувствителен к регистру символов."""
    # Для этого теста нужно иметь представление о том, как должен работать ваш поиск и что считается успешным поиском.
    # Например, тест может проверять, что поиск по разным регистрам возвращает не пустой результат.
    result = search_employees(query)
    assert (result is not None) == expected
