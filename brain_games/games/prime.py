from typing import Tuple
from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MIN_NUMBER = 1
_MAX_NUMBER = 150


def get_question() -> Tuple[int, str]:
    number = randint(_MIN_NUMBER, _MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'

    return number, answer


def is_prime(number: int) -> bool:
    if number % 2 == 0:
        return number == 2
    div = 3
    while div**2 <= number and number % div != 0:
        div += 2

    return div**2 > number


def is_right_answer(answer: str, right_answer: bool) -> bool:
    return answer == right_answer
