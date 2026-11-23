from brain_games.scripts.engine import run_game
from brain_games.games.prime import generate_round

DESCRIPTIONS = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(DESCRIPTIONS, generate_round)

if __name__ == "__main__":
    main()
