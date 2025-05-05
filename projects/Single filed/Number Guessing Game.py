import random as r

def guess(number,chances):
    print(number)
    for i in range(chances):
        gn = int(input("Type a number: "))
        if gn == number:
            print(f"Correct Answer! {number} was indeed what i was thinking")
            break
        elif gn > number:
            print("Nope a little lower!")
            chances -= 1
            print(f"Chances left = {chances}")
        elif gn < number:
            print("Nope a little higher!")
            chances -= 1
            print(f"Chances left = {chances}")
    if chances == 0:
        print("You ran out of guesses")
    x = input("Wanna Play Again?\n[1] YES\n[2] NO\n")
    if x == '1':
        main()
    else:
        print("Thanks For Playing!!!")

def main():
    print("WELCOME TO NUMBER GUESSER")
    print("I am thinking of a number between 1 and 100 guess it!!")
    x = input("Choose a difficulty\n[1] Easy\n[2] Hard\n")
    if x == '1':
        print("You have 10 chances to guess the number")
        guess(r.randint(0,100),10)
    if x == '2':
        print("You have 5 chances to guess the number")
        guess(r.randint(0,100),5)
main()