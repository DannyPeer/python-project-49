import random
def generate_round():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    first_number = number1
    second_number = number2

    while number2 != 0:
        old_number1 = number1
        number1 = number2 
        number2 = old_number1 % number2 

    question = f"{first_number} {second_number}"

    expected_answer = str(number1)

         

    return question, expected_answer
