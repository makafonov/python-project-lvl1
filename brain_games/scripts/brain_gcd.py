#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games import gcd
from brain_games.games.base import game_flow


def main():
    name = welcome_user()
    game_flow(gcd, name)


if __name__ == '__main__':
    main()
