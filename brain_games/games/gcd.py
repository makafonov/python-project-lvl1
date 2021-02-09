from typing import Tuple
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'
_MIN_NUMBER = 1
_MAX_NUMBER = 50


def get_question() -> Tuple[str, int]:
    num1 = randint(_MIN_NUMBER, _MAX_NUMBER)
    num2 = randint(_MIN_NUMBER, _MAX_NUMBER)
    answer = get_gcd(num1, num2)
    question = '{0} {1}'.format(num1, num2)

    return question, answer


def get_gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1

    return get_gcd(num2, num1 % num2)


def is_right_answer(answer: str, right_answer: int) -> bool:
    if answer.isdigit() and int(answer) == right_answer:
        return True

    return False
