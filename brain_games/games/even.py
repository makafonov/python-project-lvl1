from random import randint
from typing import Optional, Tuple


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def get_question() -> Tuple[int, str]:
    question = randint(_MIN_NUMBER, _MAX_NUMBER)
    answer = 'yes' if question % 2 == 0 else 'no'

    return question, answer


def is_right_answer(answer: str, right_answer: Optional[str]) -> bool:
    return answer == right_answer
