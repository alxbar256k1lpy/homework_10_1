"""Модуль для маскирования номеров карт и счетов."""

import logging
from pathlib import Path

# Вычисляем путь к папке logs в корне проекта
base_dir = Path(__file__).resolve().parent.parent
logs_dir = base_dir / "logs"
logs_dir.mkdir(exist_ok=True)

# Настройка логгера для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(logs_dir / "masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты."""
    logger.debug("Запуск функции маскировки номера карты")
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        logger.error(f"Передан некорректный номер карты (длина {len(card_number_str)} символов)")
        return "Некорректный номер карты"

    masked_card = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.info("Номер карты успешно замаскирован")
    return masked_card


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета."""
    logger.debug("Запуск функции маскировки номера счета")
    mask_account_str = str(mask_account)
    if len(mask_account_str) != 20:
        logger.error(f"Передан некорректный номер счета (длина {len(mask_account_str)} символов)")
        return "Некорректный номер счета"

    masked_account = f"**{mask_account_str[-4:]}"
    logger.info("Номер счета успешно замаскирован")
    return masked_account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
