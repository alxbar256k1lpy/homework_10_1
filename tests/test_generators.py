"""Тесты для модуля генераторов банковских операций."""

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовым набором транзакций."""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод со счета на счет"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод с карты на карту"},
        {"id": 4, "operationAmount": {}, "description": "Перевод организации"},
    ]


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("RUB", [2]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(sample_transactions, currency, expected_ids):
    """Тестирует фильтрацию транзакций по заданной валюте."""
    gen = filter_by_currency(sample_transactions, currency)
    result_ids = [tx["id"] for tx in gen]
    assert result_ids == expected_ids


def test_filter_by_currency_empty():
    """Тестирует работу фильтра валюты на пустом списке."""
    gen = filter_by_currency([], "USD")
    assert list(gen) == []


@pytest.mark.parametrize(
    "input_data, expected_descriptions",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Описание отсутствует"],
        ),
        ([], []),
    ],
)
def test_transaction_descriptions(input_data, expected_descriptions):
    """Тестирует получение описаний транзакций."""
    gen = transaction_descriptions(input_data)
    assert list(gen) == expected_descriptions


@pytest.mark.parametrize(
    "start, stop, expected_cards",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start, stop, expected_cards):
    """Тестирует генератор номеров карт в заданном диапазоне."""
    gen = card_number_generator(start, stop)
    assert list(gen) == expected_cards
