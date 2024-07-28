import random
import os
data=[
    {
        "name":'sai',
        "follower_count":200,
        "country":'India',
        "description":'techical expert'
    },
    {
        "name":'sundar',
        "follower_count":500,
        "country":'US',
        "description":'cybersecurity ananlyst'
    },
{
        "name":'krishna',
        "follower_count":400,
        "country":'India',
        "description":'veternary specialist'
    },
{
        "name":'padma',
        "follower_count":480,
        "country":'India',
        "description":'agriculture specialist'
    },
{
        "name":'ram',
        "follower_count":700,
        "country":'Dubai',
        "description":'software engineer'
    }
]
score=0
def display_accountinfo(account):
    name=account["name"],
    country=account["country"]
    description=account["description"]
    return f"{name}, a{description} from {country}"
def check_answer(guess,follower_1,follower_2):
    if follower_1<follower_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

account_2=random.choice(data)
continue_flag=True
while continue_flag:
    account_1=account_2
    account_2=random.choice(data)
    while account_1==account_2:
        account_2=random.choice(data)
    print(f"Compare 1:{display_accountinfo(account_1)}")
    print("vsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvs")
    print(f"Compare 2:{display_accountinfo(account_2)}")
    guess=int(input("enter who has highest followers"))
    follower_count_1=account_1["follower_count"]
    follower_count_2=account_2["follower_count"]
    is_correct=check_answer(guess,follower_count_1,follower_count_2)
    os.system('cls')

    if is_correct:
        score+=1
        print(f"you are right ,your score is {score}")
    else:
        print(f"you are wrong ,your final score{score}")
        continue_flag=False
