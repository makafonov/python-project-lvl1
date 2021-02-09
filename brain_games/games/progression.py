from typing import Tuple
from random import randint

RULES = 'What number is missing in the progression?'
_MIN_NUMBER = 1
_MAX_NUMBER = 10
_PROGRESSION_LENGTH = 10


def get_question() -> Tuple[str, int]:
    start = randint(_MIN_NUMBER, _MAX_NUMBER)
    step = randint(_MIN_NUMBER, _MAX_NUMBER)
    index = randint(0, _PROGRESSION_LENGTH - 1)
    progression = [start]
    for _ in range(_PROGRESSION_LENGTH - 1):
        start += step
        progression.append(start)
    answer = progression[index]
    progression[index] = '..'  # type: ignore

    return ' '.join(map(str, progression)), answer


def is_right_answer(answer: str, right_answer: int) -> bool:
    if answer.isdigit() and int(answer) == right_answer:
        return True

    return False
