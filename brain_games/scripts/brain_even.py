from brain_games.games.even import generate_round
from brain_games.scripts.engine import run_game

DESCRIPTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()









