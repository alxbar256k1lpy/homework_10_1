"""Глобальные фикстуры для тестирования модулей."""

import pytest


@pytest.fixture
def valid_card_number() -> str:
    """Фикстура, генерирующая корректный 16-значный номер карты."""
    return "7000792289606361"


@pytest.fixture
def valid_account_number() -> str:
    """Фикстура, генерирующая корректный 20-значный номер счета."""
    return "73654108430135874305"


@pytest.fixture
def valid_visa_card() -> str:
    """Фикстура, генерирующая корректную строку с картой Visa."""
    return "Visa Gold 5999414228426353"


@pytest.fixture
def valid_widget_account() -> str:
    """Фикстура, генерирующая корректную строку со счетом."""
    return "Счет 73654108430135874305"


@pytest.fixture
def valid_iso_date() -> str:
    """Фикстура, генерирующая корректную ISO-строку даты."""
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def raw_operations_data() -> list[dict]:
    """Глобальная фикстура со всеми возможными комбинациями state и date."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 11111111, "state": "PENDING", "date": "2023-01-01T00:00:00.000000"},
        {"id": 22222222, "state": "EXECUTED"},  # Ветка: Есть статус, НО нет даты
        {"id": 33333333, "date": "2025-12-31T23:59:59.000000"},  # Ветка: Нет статуса, НО есть дата
        {},  # Ветка: Абсолютно пустой словарь (граничный случай)
    ]


@pytest.fixture
def duplicate_dates_data() -> list[dict]:
    """Фикстура с операциями, имеющими абсолютно одинаковую дату."""
    return [
        {"id": 10, "state": "EXECUTED", "date": "2026-08-26T12:00:00.000000"},
        {"id": 20, "state": "EXECUTED", "date": "2026-08-26T12:00:00.000000"},
    ]
