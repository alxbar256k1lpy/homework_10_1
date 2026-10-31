import unittest
from unittest.mock import patch, mock_open
import json
from src.utils import get_financial_transactions


class TestUtils(unittest.TestCase):

    def test_get_transactions_success(self):
        """Тест: успешное чтение корректного списка транзакций."""
        test_data = [{"id": 1, "state": "EXECUTED"}]
        mock_json = json.dumps(test_data)

        with patch("builtins.open", mock_open(read_data=mock_json)):
            result = get_financial_transactions("fake_path.json")
            self.assertEqual(result, test_data)

    def test_get_transactions_file_not_found(self):
        """Тест: файл не найден -> возвращается пустой список."""
        result = get_financial_transactions("non_existent_file.json")
        self.assertEqual(result, [])

    def test_get_transactions_not_a_list(self):
        """Тест: в файле лежит словарь, а не список -> возвращается пустой список."""
        test_data = {"key": "value"}
        mock_json = json.dumps(test_data)

        with patch("builtins.open", mock_open(read_data=mock_json)):
            result = get_financial_transactions("fake_path.json")
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
