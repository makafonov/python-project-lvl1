#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.scripts.games import even


def main():
    name = welcome_user()
    even.start_game(name)


if __name__ == '__main__':
    main()
