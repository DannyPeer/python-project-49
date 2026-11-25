from brain_games.games.prime import generate_round
from brain_games.engine import run_game

DESCRIPTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()
