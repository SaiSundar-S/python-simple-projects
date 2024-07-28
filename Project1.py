import random
import rockpaperscissor

user=int(input("enter your choice: 0 for rock , 1 for paper, 2 for scissors"))

if user<0 or user>=3:
    print("invalid choice and you lose :(")
else:
    print(rockpaperscissor.games_images[user])
    computer=random.randint(0,2)
    print(computer)
    print(rockpaperscissor.games_images[computer])
    if user==0 and computer==2:
         print("You Win!!")
    elif user==2 and computer==0:
        print("You lose")
    elif user==computer:
        print("Draw")
    elif user>computer:
        print("You WIn!!")
    elif user<computer:
        print("you Lose")

