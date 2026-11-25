from brain_games.games.calc import generate_round
from brain_games.scripts.engine import run_game

DESCRIPTIONS = "What is the result of the expression?"


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()


