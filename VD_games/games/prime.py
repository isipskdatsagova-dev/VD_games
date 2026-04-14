Игра "Простое ли число?" — определить, является ли число простым.

import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    """Генерирует число и правильный ответ (yes/no)."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer


if __name__ == "__main__":
    print(RULES)
    q, a = generate_round()
    print(f"Question: {q}")
    print(f"Answer: {a}")
