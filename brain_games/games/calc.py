from typing import Tuple
from random import randint, choice

import operator

RULES = 'What is the result of the expression?'
_MIN_NUMBER = 0
_MAX_NUMBER = 10
_OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_question() -> Tuple[str, int]:
    operand_one = randint(_MIN_NUMBER, _MAX_NUMBER)
    operand_two = randint(_MIN_NUMBER, _MAX_NUMBER)
    operation = choice(list(_OPERATIONS.keys()))
    answer = _OPERATIONS[operation](operand_one, operand_two)
    question = '{0} {1} {2}'.format(operand_one, operation, operand_two)

    return question, answer


def is_right_answer(answer: str, right_answer: int) -> bool:
    if answer.lstrip('-').isdigit() and int(answer) == right_answer:
        return True

    return False
