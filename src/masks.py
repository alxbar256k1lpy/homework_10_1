"""Модуль для маскирования номеров карт и счетов."""

def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты."""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Некорректный номер карты"

    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета."""
    mask_account_str = str(mask_account)
    if len(mask_account_str) != 20:
        return "Некорректный номер счета"

    return f"**{mask_account_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
