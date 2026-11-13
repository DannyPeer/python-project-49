import random
from brain_games.scripts.engine import run_game
DESCRIPTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'
def generate_round():
    number = random.randint(1, 100)

    if number % 2 == 0:
        expected_answer = "yes"
    else:
        expected_answer = "no"

    question = str(number)

    return question, expected_answer






def main():
    run_game(DESCRIPTIONS, generate_round)

if __name__ == "__main__":
    main()









