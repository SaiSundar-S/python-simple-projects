import random
import hangman_stages
import word_file

lives=int(input("enter the number lives given to hangman"))
chosen_word=random.choice(word_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter")
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
      lives-=1
      if lives==0:
        game_over=True
        print("You lose")
    if '_'  not in display:
        game_over=True
        print("you Win!!")
    print(hangman_stages.stages[lives])
