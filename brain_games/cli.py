import prompt


def welcome_user() -> None:
    """Приветствие игрока."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
