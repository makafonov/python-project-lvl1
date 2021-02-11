from typing import Tuple
from random import randint, choice

import operator

RULE = 'What is the result of the expression?'
_MIN_NUMBER = 0
_MAX_NUMBER = 10
_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question_and_answer() -> Tuple[str, int]:
    """Формирование вопроса и правильного ответа для раунда игры."""
    operand_one = randint(_MIN_NUMBER, _MAX_NUMBER)
    operand_two = randint(_MIN_NUMBER, _MAX_NUMBER)
    operation = choice(list(_OPERATIONS.keys()))
    answer = _OPERATIONS[operation](operand_one, operand_two)
    question = '{0} {1} {2}'.format(operand_one, operation, operand_two)

    return question, answer
