import random
def generate_round():
    number = random.randint(1, 100)

    if number % 2 == 0:
        expected_answer = "yes"
    else:
        expected_answer = "no"

    question = str(number)

    return question, expected_answer