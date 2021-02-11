#!/usr/bin/env python
import prompt
from brain_games.games import calc as game
from brain_games.game_flow import start_game


def main():
    """Функция, запускающая игру."""
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(player_name))
    start_game(game, player_name)


if __name__ == '__main__':
    main()
