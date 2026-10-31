"""Модуль для конвертации валют транзакций через внешнее API."""

import os

import requests
from dotenv import load_dotenv

# Загружаем переменные из скрытого файла .env, который лежит в корне
load_dotenv()


def convert_transaction_to_rub(transaction):
    """Принимает транзакцию и возвращает сумму операции в рублях."""
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0.0))
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return amount

    if currency_code in ["USD", "EUR"]:
        api_key = os.getenv("API_KEY")
        headers = {"apikey": str(api_key)}

        url = f"https://apilayer.com{currency_code}"

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                rate = float(data.get("rates", {}).get("RUB", 1.0))
                return amount * rate

        except requests.RequestException:
            return 0.0

    return 0.0
