import prompt

_ATTEMPTS = 3
_UNSUCCESSFUL_MESSAGE = (
    "'{0}' is wrong answer ;(. Correct answer was '{1}'\n"
    "Let's try again, {2}!"
)


def start_game(game) -> None:
    """Игровой движок, описывающий общий порядок выполнения игр."""
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    print(game.RULE)
    for _ in range(_ATTEMPTS):
        question, right_answer = game.get_question_and_answer()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer != str(right_answer):
            print(
                _UNSUCCESSFUL_MESSAGE.format(answer, right_answer, player_name)
            )
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(player_name))
