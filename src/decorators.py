from functools import wraps


def log(filename=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                message = f"{func.__name__} {e}. Inputs: {args}, {kwargs}"
            else:
                message = f"{func.__name__} ok"

            if filename == "" :
                print(message)
            else:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")

        return wrapper

    return decorator
