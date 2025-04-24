bidders = {}
bidvalue = 0
print(r''' 
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
print("Welcome to khufiya Auctions")
while True:
    name = input("Name of the bidder: ")
    amount = int(input("Amount you want to bid(in ruppees): "))
    bidders[name] = amount
    choice = input("Anyone else who want to bid? Type 'yes' or 'no': ")
    if choice == "yes":
        continue
    elif choice == "no":
        break
for i in bidders:
    if bidders[i] > bidvalue:
        bidvalue =  bidders[i]
        bidwinner = i
print(f"{bidwinner} won the auction with an amount of {bidvalue} rupees!")