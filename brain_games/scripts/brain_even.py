from brain_games.cli import welcome_user
import random
def game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)

        if number % 2 == 0:
            expected_answer = "yes"
        else:
            expected_answer = "no"
    
        print(f"Question: {number}")
        answer = input("Your answer: ")
    
        if answer == expected_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'.")
            print(f"Let's try again, {name}")
            return False
 
    print(f"Congratulations, {name}!")
    return True

def main():
    game()

if __name__ == "__main__":
    main()



    
        


    

    