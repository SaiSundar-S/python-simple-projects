import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def check_difficulty(level):
    if level=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right.. the answer is {answer}")
def game():
    print("let me think the number id between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("choose your difficulty ...Type easy or hard")
    attempts=check_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("invalid input ...play again")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} remaining to guess a number")
        guessed_number=int(input("Guess a number"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("you are out of guess..you loose")
            return
        elif guessed_number!=answer:
            print("guess again")

game()

