from brain_games.games.gcd import generate_round
from brain_games.scripts.engine import run_game

DESCRIPTIONS = "Find the greatest common divisor of given numbers."


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()
