#!/usr/bin/env python
from brain_games.games import gcd
from brain_games.game_flow import start_game


def main():
    """Функция, запускающая игру."""
    start_game(gcd)


if __name__ == '__main__':
    main()
