from random import randint
from typing import Optional, Tuple

import prompt

_ATTEMPTS = 3


def start_game(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(_ATTEMPTS):
        number = randint(0, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        is_right_answer, right_answer = check_answer(number, answer)
        if not is_right_answer:
            print(
                '\n'.join(
                    [
                        "'{0}' is wrong answer ;(. Correct answer was '{1}'"
                        .format(answer, right_answer),
                        "Let's try again, {0}!".format(name)
                    ]
                )
            )
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(name))


def check_answer(number: int, answer: Optional[str]) -> Tuple[bool, str]:
    right_answer = 'yes' if number % 2 == 0 else 'no'
    if answer == right_answer:
        return True, right_answer
    return False, right_answer
