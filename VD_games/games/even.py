"""Игра "Проверка на чётность"."""

import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
