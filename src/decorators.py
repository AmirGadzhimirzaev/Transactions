from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор для автоматической регистрации информации о выполнение функций"""

    def decorator(func: Callable) -> Callable:
        def place_for_message(message: str) -> None:
            if filename == "":
                print(message)
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                func(*args, **kwargs)
            except Exception as e:
                place_for_message(f"{func.__name__} {e}. Inputs: {args}, {kwargs}")
            else:
                place_for_message(f"{func.__name__} ok")
                return func(*args, **kwargs)

        return wrapper

    return decorator
