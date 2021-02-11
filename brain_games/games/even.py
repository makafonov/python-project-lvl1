from random import randint
from typing import Tuple


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def get_question_and_answer() -> Tuple[int, str]:
    """Формирование вопроса и правильного ответа для раунда игры."""
    question = randint(_MIN_NUMBER, _MAX_NUMBER)
    answer = 'yes' if question % 2 == 0 else 'no'

    return question, answer
