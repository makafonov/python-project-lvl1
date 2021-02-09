#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games import calc
from brain_games.games.base import game_flow


def main():
    name = welcome_user()
    game_flow(calc, name)


if __name__ == '__main__':
    main()
