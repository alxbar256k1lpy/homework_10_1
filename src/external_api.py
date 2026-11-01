"""Модуль для конвертации валют транзакций через внешнее API."""


import requests
from dotenv import load_dotenv


load_dotenv()


def convert_transaction_to_rub(transaction):
    """Принимает транзакцию и возвращает сумму операции в рублях (float)."""
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0.0))
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return round(amount, 2)

    if currency_code in ["USD", "EUR"]:
        api_key = os.getenv("API_KEY")
        headers = {"apikey": str(api_key)}
        url = f"https://apilayer.com{currency_code}&amount={amount}"

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if data.get("success") is True and "result" in data:
                    converted_amount = data.get("result", 0.0)
                    return round(float(converted_amount), 2)
                return 0.0

        except requests.RequestException:
            return 0.0

    return 0.0


if __name__ == "__main__":
    import os

    from src.utils import get_financial_transactions

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.normpath(os.path.join(current_dir, "..", "data", "operations.json"))

    transactions = get_financial_transactions(json_path)
    print(f"Total: {len(transactions)}")

    if transactions:
        for index, op in enumerate(transactions, 1):
            res = convert_transaction_to_rub(op)
            print(f"#{index} Amount in RUB: {res}")
