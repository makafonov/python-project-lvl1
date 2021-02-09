import prompt

_ATTEMPTS = 3


def game_flow(game, player_name: str) -> None:
    print(game.RULES)
    for _ in range(_ATTEMPTS):
        question, right_answer = game.get_question()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if not game.is_right_answer(answer, right_answer):
            print(
                '\n'.join(
                    [
                        "'{0}' is wrong answer ;(. Correct answer was '{1}'"
                        .format(answer, right_answer),
                        "Let's try again, {0}!".format(player_name)
                    ]
                )
            )
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(player_name))
