import random

def generate_round():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    symbol = random.choice(["+", "-", "*"])

    if symbol == "+":
        result = number1 + number2
    elif symbol == "-":
        result = number1 - number2
    else:
        result = number1 * number2

    question = f"{number1} {symbol} {number2}"

    expected_answer = str(result)

    return question, expected_answer
