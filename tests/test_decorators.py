"""Тесты для проверки декоратора логирования."""

import pytest

from src.decorators import log


def test_log_console_success(capsys):
    """Тест успешного выполнения функции с выводом в консоль."""

    @log()
    def add(x, y):
        return x + y

    assert add(2, 3) == 5

    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_console_error(capsys):
    """Тест вызова ошибки в функции с выводом в консоль."""

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert captured.out.strip() == "divide error: ZeroDivisionError. Inputs: (10, 0), {}"


def test_log_file_success(tmp_path):
    """Тест успешного выполнения с записью в файл."""
    test_file = tmp_path / "test_success.txt"

    @log(filename=str(test_file))
    def greet(name):
        return f"Hello, {name}"

    assert greet("Alex") == "Hello, Alex"

    assert test_file.read_text(encoding="utf-8") == "greet ok\n"


def test_log_file_error(tmp_path):
    """Тест вызова ошибки с записью в файл."""
    test_file = tmp_path / "test_error.txt"

    @log(filename=str(test_file))
    def get_element(lst, index):
        return lst[index]

    with pytest.raises(IndexError):
        get_element([], 5)

    expected_log = "get_element error: IndexError. Inputs: ([], 5), {}\n"
    assert test_file.read_text(encoding="utf-8") == expected_log
