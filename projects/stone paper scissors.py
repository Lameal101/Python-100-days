import random as r
choices = ["STONE","PAPER","SCISSORS"]
print("WELCOME TO STONE PAPER SCISSORS\nPick one:")
def main():
    score = 0
    computer_score = 0
    again = 1
    while again:
        pick = choices[int(input("[1] STONE\n[2] PAPER\n[3] SCISSORS\n: "))-1]
        computer_pick = choices[r.randint(0,2)]
        print(f"You chose {pick}")
        print(f"Computer chose {computer_pick}")
        if pick == computer_pick:
            print("Both chose the same")
        elif pick == "STONE" and computer_pick == "PAPER":
            computer_score += 1
            print("Computer Scored")
        elif pick == "STONE" and computer_pick == "SCISSORS":
            score += 1
            print("You Scored")
        elif pick == "SCISSORS" and computer_pick == "STONE":
            computer_score += 1
            print("Computer Scored")
        elif pick == "SCISSORS" and computer_pick == "PAPER":
            score += 1
            print("You Scored")
        elif pick == "PAPER" and computer_pick == "SCISSORS":
            computer_score += 1
            print("Computer Scored")
        elif pick == "PAPER" and computer_pick == "STONE":
            score += 1
            print("You Scored")
        else:
            print("Choose a correct option.\n")
        again = bool(int(input("Wanna Play Again:\n[1]NO\n[2]YES\n"))-1)
    print("GAME OVER")
    print(f"You Scored {score}")
    print(f"Computer Scored {computer_score}")
main()