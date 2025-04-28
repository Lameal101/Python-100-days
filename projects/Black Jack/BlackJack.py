import random as r
import elements as e

def again():
    while True:
        choose = input("Wanna Play Again:\n[1] YES\n[2] NO\n")
        if choose == '1':
            play()
            break
        elif choose == '2':
            menu()
            break
        else:
            print("Choose a correct option!")
            continue

def play():   #initial stage
    player_cards = [r.choice(e.cards()),r.choice(e.cards())]
    dealer_cards = [r.choice(e.cards()),r.choice(e.cards()),]
    print(f"Your cards:{player_cards}")
    print(f"Dealers cards:[{dealer_cards[0]}{(len(dealer_cards)-1) * ',_'}]")
    player_dealing(player_cards,dealer_cards)

def player_dealing(player_cards,dealer_cards):
    while True:
        choose = input("Your turn\n[1] Hit\n[2] Keep\n:")
        x = r.choice(e.cards())
        if choose == "1":
            if x == 11 and (21 - sum(player_cards)) < 11:
                x = 1
            player_cards.append(x)
            print(f"Your cards:{player_cards}")
            print(f"Dealers cards:[{dealer_cards[0]}{(len(dealer_cards) - 1) * ',_'}]")
            computer_dealing(player_cards, dealer_cards)
            break
        elif choose == "2":
            compare(player_cards,dealer_cards)
            computer_dealing(player_cards, dealer_cards)
            break
        else:
            print("Choose a correct option!!")
            continue

def computer_dealing(player_cards,dealer_cards):
    if (21 - sum(dealer_cards)) < 11 and sum(dealer_cards) < 21:
        print("Dealer asks for another card!")
        x = r.choice(e.cards())
        dealer_cards.append(x)
        print(f"Your cards:{player_cards}")
        print(f"Dealers cards:[{dealer_cards[0]}{(len(dealer_cards) - 1) * ',_'}]")
        player_dealing(player_cards, dealer_cards)
    else:
        print("Dealer Keeps!")
        print(f"Your cards:{player_cards}")
        print(f"Dealers cards:[{dealer_cards[0]}{(len(dealer_cards) - 1) * ',_'}]")
        player_dealing(player_cards, dealer_cards)

def A_card(cards):
    for i in range(len(cards)):
        if cards[i] == 11 and sum(cards) > 21:
            cards.pop(i)
            cards.append(1)
    return cards
def compare(player_cards,dealer_cards):
    print(f"Your cards:{player_cards}")
    print(f"Your Total: {sum(player_cards)}")
    print(f"Dealer cards:{dealer_cards}")
    print(f"Dealer Total: {sum(dealer_cards)}")
    player_cards = A_card(player_cards)
    dealer_cards = A_card(dealer_cards)
    if sum(player_cards) > 21:
        print("You lost")
    elif (21 - sum(player_cards)) < (21 - sum(dealer_cards)):
        print("You Won!")
    elif sum(player_cards) == sum(dealer_cards):
        print("It is a Draw!")
    elif (21 - sum(player_cards)) > (21 - sum(dealer_cards)):
        print("Dealer Won!")
    again()

def menu(): #menu,title
    print(e.title())
    while True:
        print(e.menu())
        choose = input("Choose a option!!\n:")
        if choose == '1':
            play()
            break
        elif choose == '2':
            print(e.instructions())
            continue
        elif choose == '3':
            print("THANKS FOR PLAYING")
            exit()
        else:
            print("Choose correct option from the menu")
            continue
menu()