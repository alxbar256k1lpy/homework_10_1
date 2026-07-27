"""Модуль с функциями для обработки данных виджета."""

from masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Принимает строку с типом и номером карты или счета и возвращает её маску."""
    if "счет" in number.lower():
        return f"Счет {get_mask_account(number[-20:])}"

    return f"{number[:-17]} {get_mask_card_number(number[-16:])}"


def get_date(date_string: str) -> str:
    """Принимает строку с датой в ISO-формате и возвращает её в формате ДД.ММ.ГГГГ."""
    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
