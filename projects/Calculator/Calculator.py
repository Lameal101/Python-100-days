import Calc as c
print(c.head())
print("CALCULATOR")
def operations(num1,opr,num2):
    if opr == '+':
        sol = num1 + num2
    elif opr == '-':
        sol = num1 - num2
    elif opr == '*':
        sol = num1 * num2
    elif opr == '/':
        sol = num1 / num2
    else:
        print("Invalid input given")
        return None
    return sol

def new():
    num1 = int(input("Type the first number: "))
    opr = input("Type the operation\n[+] [-] [*] [/]\n")
    num2 = int(input("Type the second number: "))
    sol = operations(num1,opr,num2)
    output(sol)
def same(sol):
    opr = input("Type the operation\n[+] [-] [*] [/]\n")
    num2 = int(input("Type the second number: "))
    sol = operations(sol,opr,num2)
    output(sol)
def output(sol):
    print(f"Output: {sol}")
    choose = int(input("[1] Operation on the same number\n[2] Operation on new number\n"))
    if choose == 1:
        same(sol)
    elif choose == 2:
        new()
    else:
        print("Type a correct number")
new()