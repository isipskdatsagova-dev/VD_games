"""Игра "Калькулятор" — вычислить результат арифметического выражения."""

import random
import prompt


def generate_question():
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


def run_game():
    """Основная логика игры."""
    print("Welcome to the VD games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    run_game()
