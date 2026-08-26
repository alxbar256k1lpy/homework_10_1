"""Тесты для функций фильтрации и сортировки операций."""

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 3),  # С новой фикстурой теперь находит 3 элемента
        ("CANCELED", 1),  # Находит 1 элемент
        ("PENDING", 1),  # Находит 1 элемент
    ],
)
def test_filter_by_state_various_statuses(raw_operations_data, state, expected_count):
    """Параметризованное тестирование фильтрации по различным значениям статуса state."""
    result = filter_by_state(raw_operations_data, state)
    assert len(result) == expected_count
    for item in result:
        assert item.get("state") == state


def test_filter_by_state_missing(raw_operations_data):
    """Проверка работы функции при отсутствии словарей с указанным статусом в списке."""
    result = filter_by_state(raw_operations_data, "NON_EXISTENT_STATUS")
    assert result == []


def test_sort_by_date_descending(raw_operations_data):
    """Тестирование сортировки списка словарей по датам в порядке убывания (reverse=True)."""
    result = sort_by_date(raw_operations_data, reverse=True)
    assert result[0]["id"] == 33333333
    assert result[1]["id"] == 11111111
    assert result[2]["id"] == 41428829
    assert result[3]["id"] == 594226727
    assert result[4]["id"] == 939719570


def test_sort_by_date_ascending(raw_operations_data):
    """Тестирование сортировки списка словарей по датам в порядке возрастания (reverse=False)."""
    result = sort_by_date(raw_operations_data, reverse=False)
    assert result[-5]["id"] == 939719570
    assert result[-4]["id"] == 594226727
    assert result[-3]["id"] == 41428829
    assert result[-2]["id"] == 11111111
    assert result[-1]["id"] == 33333333


def test_sort_by_date_equal_dates(duplicate_dates_data):
    """Проверка корректности сортировки при одинаковых датах (стабильность исходного порядка)."""
    result = sort_by_date(duplicate_dates_data, reverse=True)
    assert result[0]["id"] == 10
    assert result[1]["id"] == 20


@pytest.mark.parametrize(
    "invalid_data, expected_first_id",
    [
        (
            [
                {"id": 100, "date": ""},
                {"id": 200, "date": "2023-01-01"},
            ],
            200,
        ),
        (
            [
                {"id": 300},
                {"id": 400, "date": "2023-01-01"},
            ],
            400,
        ),
    ],
)
def test_sort_by_date_invalid_and_missing_formats(invalid_data, expected_first_id):
    """Тесты на работу функции с некорректными, пустыми или отсутствующими форматами дат."""
    result = sort_by_date(invalid_data, reverse=True)
    assert result[0]["id"] == expected_first_id


def test_filter_by_state_with_missing_keys(raw_operations_data):
    """Тестирование ветки кода, когда у словарей в списке отсутствует ключ 'state' или словарь пуст."""
    filtered_data = filter_by_state(raw_operations_data, "EXECUTED")
    assert len(filtered_data) == 3


def test_sort_by_date_with_missing_dates(raw_operations_data):
    """Тестирование ветки кода сортировки, когда у элементов отсутствует ключ 'date'."""
    sorted_data = sort_by_date(raw_operations_data, reverse=True)
    assert sorted_data[-1] == {}
    assert sorted_data[-2]["id"] == 22222222
