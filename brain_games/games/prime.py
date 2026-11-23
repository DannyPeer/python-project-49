import random
def generate_round():
    number = random.randint(1, 20)
    expected_answer = "yes"
    if number < 2:
        expected_answer = "no"
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                expected_answer = "no"
                break

    question = str(number)
    return question, expected_answer