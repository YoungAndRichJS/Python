# 숫자 맞히기 게임

import random

def guessing_game():
    answer = random.randint(0,100)
    chance = 3

    while chance != 0 :
        print(f"You got {chance} chance(s) more !")
        user_guess = int(input("Guess the number(0~100) > "))

        if user_guess < answer:
            print("Too low...")
        if user_guess > answer:
            print("Too high...")
        if user_guess == answer:
            print(f"The answer is {answer}! Congratulation!")
            break
        chance -= 1
        
    if chance == 0:
        print(f"the answer was {answer}.")

guessing_game()