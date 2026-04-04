"""Точка входа для игры "Арифметическая прогрессия"."""

from VD_games.engine import run_game
from VD_games.games import progression


def main():
    run_game(progression)


if __name__ == "__main__":
    main()
