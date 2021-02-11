from typing import Tuple
from random import randint

RULE = 'What number is missing in the progression?'
_MIN_NUMBER = 1
_MAX_NUMBER = 10
_PROGRESSION_LENGTH = 10


def get_question_and_answer() -> Tuple[str, int]:
    """Формирование вопроса и правильного ответа для раунда игры."""
    start = randint(_MIN_NUMBER, _MAX_NUMBER)
    step = randint(_MIN_NUMBER, _MAX_NUMBER)
    index = randint(0, _PROGRESSION_LENGTH - 1)
    progression = [start + step * num for num in range(_PROGRESSION_LENGTH)]
    answer = progression[index]
    progression[index] = '..'  # type: ignore

    return ' '.join(map(str, progression)), answer
