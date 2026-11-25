from brain_games.engine import run_game
from brain_games.games.even import generate_round

DESCRIPTIONS = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(DESCRIPTIONS, generate_round)


if __name__ == "__main__":
    main()









