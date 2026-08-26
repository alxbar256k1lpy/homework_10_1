"""Тесты для функций маскирования карт и счетов."""

import pytest

# Замените имя_вашего_модуля на имя файла, где лежат ваши функции
from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number_correct_masking(valid_card_number):
    """Тестирование правильности маскирования корректного номера карты (с фикстурой)."""
    assert get_mask_card_number(valid_card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),  # Другой формат цифр
        ("1111222233334444", "1111 22** **** 4444"),  # Граничные значения цифр
    ],
)
def test_get_mask_card_number_formats(card_number, expected):
    """Проверка работы функции на различных входных форматах правильных номеров карт."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card_number", ["123456789012345"])
def test_get_mask_card_number_lengths(invalid_card_number):
    """Проверка работы функции на нестандартных длинах номеров карт."""
    assert get_mask_card_number(invalid_card_number) == "Некорректный номер карты"


@pytest.mark.parametrize(
    "missing_card_input",
    [
        "",
    ],
)
def test_get_mask_card_number_missing(missing_card_input):
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    assert get_mask_card_number(missing_card_input) == "Некорректный номер карты"


def test_get_mask_account_correct_masking(valid_account_number):
    """Тестирование правильности маскирования корректного номера счета (с фикстурой)."""
    assert get_mask_account(valid_account_number) == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("99999999999999999999", "**9999"),
    ],
)
def test_get_mask_account_formats(account_number, expected):
    """Проверка работы функции с различными форматами корректных номеров счетов."""
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "short_account_number",
    [
        "1234567890123456789",
        "12345",
        "",
    ],
)
def test_get_mask_account_short_lengths(short_account_number):
    """Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины."""
    assert get_mask_account(short_account_number) == "Некорректный номер счета"


@pytest.mark.parametrize(
    "long_account_number",
    [
        "123456789012345678901",
    ],
)
def test_get_mask_account_long_lengths(long_account_number):
    """Проверка работы функции, если длина номера счета больше ожидаемой."""
    assert get_mask_account(long_account_number) == "Некорректный номер счета"
