


# Задание№4
# Написать параметризуемый декоратор с именем repeat, который выполняет декорируемую функцию заданное количество раз.
#
# Это достаточно распространённая задача в сфере тестирования.
#
# Функция параметризации декораторов repeat принимает необязательным аргументом количество вызовов декорируемой функции.
#
#     Количество вызовов декорируемой функции должно быть позиционно-ключевым аргументом, передаётся в виде объекта int, значение по умолчанию 2.
#
# Декоратор может применяться к функциям с различным набором позиционных и ключевых аргументов.
#
# Написанный декоратор необходимо протестировать вручную с помощью дополнительной произвольной функции.
# Пример ручного теста:
#     >>> def testing_function():
#     ...     print('python')
#     ...
#     >>> testing_function = repeat(testing_function)(4)
#     >>>
#     >>>
#     >>> testing_function()
#     python
#     python
#     python
#     python

from functools import wraps
from typing import Callable


def repeat(n: int = 2) -> Callable:


    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator



if __name__ == "__main__":

    @repeat(3)
    def greet(name: str) -> None:
        print(f"Hi, {name}!")


    greet("Eduard")

    @repeat()
    def add(a: int, b: int) -> int:
        result = a + b
        print(f"The result of {a} + {b} is {result}")
        return result

    add(8, 23)
