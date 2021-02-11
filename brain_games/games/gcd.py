from typing import Tuple
from random import randint

RULE = 'Find the greatest common divisor of given numbers.'
_MIN_NUMBER = 1
_MAX_NUMBER = 50


def get_question_and_answer() -> Tuple[str, int]:
    """Формирование вопроса и правильного ответа для раунда игры."""
    num1 = randint(_MIN_NUMBER, _MAX_NUMBER)
    num2 = randint(_MIN_NUMBER, _MAX_NUMBER)
    answer = get_gcd(num1, num2)
    question = '{0} {1}'.format(num1, num2)

    return question, answer


def get_gcd(num1: int, num2: int) -> int:
    """Вычисление наибольшего общего делителя."""
    if num2 == 0:
        return num1

    return get_gcd(num2, num1 % num2)
