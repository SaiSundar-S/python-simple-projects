
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

dict={
      '+':add,
      '-':sub,
      '*':mul,
       '/':div
}
def calculator():
    first_number=float(input("enter first number"))
    continue_flag=True
    while continue_flag:
        for sym in dict:
            print(sym)
        symbol=input("enter your requires operator")
        if symbol not in dict:
            print("invalid symbol")
            continue_flag=False
            exit(0)
        else:
            second_number=float(input("enter second number"))
            result=dict[symbol](first_number,second_number)
        print(f"{first_number}{symbol}{second_number}={result}")

        should_continue=input("enter y to continue calculation and 'n' for new calculation and 'x' for exit")
        if should_continue=='y':
            first_number=result
        elif should_continue=='n':
            continue_flag=False
            calculator()
        else:
            continue_flag=False
            print('Bye')
calculator()