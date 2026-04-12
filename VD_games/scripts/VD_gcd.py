"""Точка входа для игры "НОД"."""

from VD_games.engine import run_game
from VD_games.games import gcd


def main():
    run_game(gcd)


if __name__ == "__main__":
    main()
