"""Модуль для работы с файлами финансовых транзакций."""

import json
import logging
from pathlib import Path

# Вычисляем путь к папке logs в корне проекта
base_dir = Path(__file__).resolve().parent.parent
logs_dir = base_dir / "logs"
logs_dir.mkdir(exist_ok=True)

# Настройка логгера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(logs_dir / "utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(file_path):
    """Принимает путь к JSON-файлу и возвращает список словарей."""
    logger.debug(f"Попытка открыть файл транзакций: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
            return data

        logger.warning(f"Данные в файле {file_path} не являются списком. Возвращен пустой список.")
        return []

    except FileNotFoundError:
        logger.error(f"Файл не найден по пути: {file_path}")
        return []
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {ex}")
        return []
