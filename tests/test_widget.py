"""Тесты для функций обработки виджета и дат."""

import pytest

from src.widget import get_date
from src.widget import mask_account_card


def test_mask_account_card_recognizes_card(valid_visa_card):
    """Проверка, что функция корректно распознает карту и применяет маску."""
    assert mask_account_card(valid_visa_card) == "Visa Gold 5999 41** **** 6353"


def test_mask_account_card_recognizes_account(valid_widget_account):
    """Проверка, что функция корректно распознает счет и применяет маску."""
    assert mask_account_card(valid_widget_account) == "Счет **4305"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card_universality(input_data, expected):
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности."""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "invalid_input, expected",
    [
        ("Visa 123", " Некорректный номер карты"),
        ("Счет 12345", "Счет Некорректный номер счета"),
        ("", " Некорректный номер карты"),
    ],
)
def test_mask_account_card_invalid_data(invalid_input, expected):
    """Тестирование функции на обработку некорректных входных данных."""
    assert mask_account_card(invalid_input) == expected


def test_get_date_correct_conversion(valid_iso_date):
    """Тестирование правильности преобразования даты из ISO-формата."""
    assert get_date(valid_iso_date) == "11.03.2024"


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2026-08-26T23:59:59.999999", "26.08.2026"),
        ("0001-01-01T00:00:00.000000", "01.01.0001"),
    ],
)
def test_get_date_formats_and_boundaries(date_string, expected):
    """Проверка работы функции на различных входных форматах и граничных случаях."""
    assert get_date(date_string) == expected


@pytest.mark.parametrize(
    "invalid_date_string, expected",
    [
        ("123", "..123"),
        ("", ".."),
    ],
)
def test_get_date_missing_and_invalid(invalid_date_string, expected):
    """Проверка работы с нестандартными строками и в случаях, когда дата отсутствует."""
    assert get_date(invalid_date_string) == expected
