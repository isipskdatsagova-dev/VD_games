"""Точка входа для игры "Проверка на чётность"."""

from VD_games.engine import run_game
from VD_games.games import even


def main():
    run_game(even)


if __name__ == "__main__":
    main()
