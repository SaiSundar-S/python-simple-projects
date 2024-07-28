import random
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','@','%','&','*','(',')','+','-']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
         'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print("welcome to password generator")
n_letters=int(input("enter the number of letters required your password"))
n_symbols=int(input("enter the number of symbols required your password"))
n_numbers=int(input("enter the number of digts required your password"))
password=[]
for i in range(1,n_letters+1):
    password+=random.choice(letters)
for i in range(1,n_numbers+1):
    password+=random.choice(numbers)
for i in range(1,n_symbols+1):
    password+=random.choice(symbols)
random.shuffle(password)
new_password=""

for char in password:
    new_password+=char

print(new_password)

