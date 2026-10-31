import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_transaction_to_rub


class TestExternalAPI(unittest.TestCase):

    def test_convert_rub(self):
        """Тест: если валюта RUB, функция сразу возвращает сумму без вызова API."""
        transaction = {
            "operationAmount": {
                "amount": "150.00",
                "currency": {"name": "руб.", "code": "RUB"}
            }
        }
        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 150.0)

    @patch("src.external_api.requests.get")
    def test_convert_usd_success(self, mock_get):
        """Тест: успешный перехват запроса к API и конвертация USD в рубли."""
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "USD", "code": "USD"}
            }
        }

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response

        result = convert_transaction_to_rub(transaction)

        self.assertEqual(result, 7500.0)
        mock_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
