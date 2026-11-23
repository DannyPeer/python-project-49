import random

from brain_games.scripts.engine import run_game

DESCRIPTIONS = "What number is missing in the progression?"


def generate_round():
    progression = []
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = random.randint(5, 10)
    for i in range(length):
        progression.append(start + step * i)
    progression, element = count_number(progression)
    question = " ".join(map(str, progression))
    expected_answer = str(element)
    return question, expected_answer


def count_number(progression):
    position = random.randint(0, len(progression) - 1)
    element = progression[position]
    progression[position] = ".."
    return progression, element


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()