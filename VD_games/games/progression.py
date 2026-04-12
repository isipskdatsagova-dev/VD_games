"""Игра "Арифметическая прогрессия" — найти пропущенное число."""

import random


RULES = "What number is missing in the progression?"


def generate_round()
    length = random.randint(5, 12)
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))
    return question, correct_answer


if __name__ == "__main__":
    print(RULES)
    q, a = generate_round()
    print(f"Question: {q}")
    print(f"Answer: {a}")
