"""Модуль с декораторами для логирования работы функций."""

from functools import wraps


def log(filename=None):
    """Декоратор для логирования работы функций в консоль или файл строго по ТЗ."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            inputs_str = f"Inputs: {args}, {kwargs}"

            try:
                result = func(*args, **kwargs)

                log_message = f"{func.__name__} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())

                return result

            except Exception as e:
                error_type = type(e).__name__

                log_message = f"{func.__name__} error: {error_type}. {inputs_str}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message.strip())

                raise e

        return wrapper

    return decorator
