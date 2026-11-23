import random

from brain_games.scripts.engine import run_game

DESCRIPTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    number = random.randint(1, 20)
    expected_answer = "yes"
    if number < 2:
        expected_answer = "no"
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                expected_answer = "no"
                break

    question = str(number)
    return question, expected_answer


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()
