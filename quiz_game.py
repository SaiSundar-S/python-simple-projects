from quiz_database import question_bank
from quiz_database import options

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("******************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    guess=input("enter your answer(A?B?C?D").upper()
    is_correct=check_answer(guess,question_bank[question_num]['answer'])

    if is_correct:
        print("Correct answer")
        score+=1
    else:
        print("incorrect Answer")
        print(f"the correct answer is {question_bank[question_num]['answer']}")
    print(f"your correct score is {score}/{question_num+1}")
print(f"you have given {score} correct answer")
print(f"your Score is{(score/len(question_bank))*100}%")