import json


def get_financial_transactions(file_path):
    """Принимает путь к JSON-файлу и возвращает список словарей с транзакциями.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []
