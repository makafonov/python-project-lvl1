#!/usr/bin/env python
from brain_games.games import calc
from brain_games.game_flow import start_game


def main():
    """Функция, запускающая игру."""
    start_game(calc)


if __name__ == '__main__':
    main()
