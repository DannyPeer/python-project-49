from brain_games.games.progression import generate_round
from brain_games.engine import run_game

DESCRIPTIONS = "What number is missing in the progression?"


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()