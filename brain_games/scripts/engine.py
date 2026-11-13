from brain_games.cli import welcome_user

ROUNDS_COUNT = 3

def run_game(description, generate_round_data):
    name = welcome_user()

    print(description)

    for _ in range(ROUNDS_COUNT):
        question, expected_answer = generate_round_data()

        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == expected_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
    

                  
