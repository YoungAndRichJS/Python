# 숫자 맞히기 게임

import random
number = random.randint(0,100)

def guessing_game():
    while True:
        user_answer = int(input("guess the number(0~100) > "))
        if type(user_answer) != int:
            print("Please enter the number ...")
        if user_answer < 0 or user_answer > 100:
            print("Please enter the number between 0 ~ 100 ...")
        if user_answer > number:
            print("Too high")
        if user_answer < number:
            print("Too low") 
        if user_answer == number:
            print(f"{user_answer} is the answer congratulation!")
            break

guessing_game()