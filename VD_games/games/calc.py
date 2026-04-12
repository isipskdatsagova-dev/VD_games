"""Игра "Калькулятор" — вычислить результат арифметического выражения."""

import random

RULES = "What is the result of the expression?"


def generate_round():
    """Генерирует случайное выражение и правильный ответ."""
    operations = [
        ('+', lambda a, b: a + b),
        ('-', lambda a, b: a - b),
        ('*', lambda a, b: a * b),
    ]
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op_symbol, op_func = random.choice(operations)
    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(op_func(num1, num2))
    return question, correct_answer
