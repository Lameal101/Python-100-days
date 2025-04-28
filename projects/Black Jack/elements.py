def title():
    return r'''
    
                  ,--,                                                                                                       
               ,---.'|                                    ,--.                 ,---._                                   ,--. 
        ,---,. |   | :      ,---,         ,----..     ,--/  /|               .-- -.' \    ,---,         ,----..     ,--/  /| 
      ,'  .'  \:   : |     '  .' \       /   /   \ ,---,': / '               |    |   :  '  .' \       /   /   \ ,---,': / ' 
    ,---.' .' ||   ' :    /  ;    '.    |   :     ::   : '/ /                :    ;   | /  ;    '.    |   :     ::   : '/ /  
    |   |  |: |;   ; '   :  :       \   .   |  ;. /|   '   ,                 :        |:  :       \   .   |  ;. /|   '   ,   
    :   :  :  /'   | |__ :  |   /\   \  .   ; /--` '   |  /                  |    :   ::  |   /\   \  .   ; /--` '   |  /    
    :   |    ; |   | :.'||  :  ' ;.   : ;   | ;    |   ;  ;                  :         |  :  ' ;.   : ;   | ;    |   ;  ;    
    |   :     \'   :    ;|  |  ;/  \   \|   : |    :   '   \                 |    ;   ||  |  ;/  \   \|   : |    :   '   \   
    |   |   . ||   |  ./ '  :  | \  \ ,'.   | '___ |   |    '            ___ l         '  :  | \  \ ,'.   | '___ |   |    '  
    '   :  '; |;   : ;   |  |  '  '--'  '   ; : .'|'   : |.  \         /    /\    J   :|  |  '  '--'  '   ; : .'|'   : |.  \ 
    |   |  | ; |   ,/    |  :  :        '   | '/  :|   | '_\.'        /  ../  `..-    ,|  :  :        '   | '/  :|   | '_\.' 
    |   :   /  '---'     |  | ,'        |   :    / '   : |            \    \         ; |  | ,'        |   :    / '   : |     
    |   | ,'             `--''           \   \ .'  ;   |,'             \    \      ,'  `--''           \   \ .'  ;   |,'     
    `----'                                `---`    '---'                "---....--'                     `---`    '---'       
                                                                                                                             
    '''
def menu():
    return '''
    [1] PLAY
    [2] INSTRUCTIONS
    [3] EXIT
    '''
def cards():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return card

def instructions():
    x = '''
    1. Objective: The goal is to get a hand value of 21 or as close as possible without going over.
    
    2. Card Values:
       - Number cards (2-10) are worth their face value.
       - Face cards (Jack, Queen, King) are worth 10 points.
       - Aces can be worth 1 or 11 points, depending on which is more beneficial for the hand.
    
    3. Dealing the Cards:
       - Each player is dealt two cards. The dealer also gets two cards, one face-up and one face-down.
    
    4. Player's Turn:
       - Players decide whether to "Hit" (take another card) or "Stand" (keep their current hand).
       - Players can keep hitting until they choose to stand or their hand value exceeds 21 (busted).
    
    5. Dealer's Turn:
       - After all players have finished, the dealer reveals the face-down card.
       - The dealer must hit if their hand is 16 or less and must stand on 17 or higher.
    
    6. Winning:
       - If your hand is closer to 21 than the dealer’s, or if the dealer busts, you win.
       - If your hand value exceeds 21, you lose.
       - If the dealer’s hand is closer to 21 or they don't bust, the dealer wins.
    
    7. Blackjack:
       - If your first two cards are an Ace and a 10-point card (10, Jack, Queen, King), you have a Blackjack and win unless the dealer also has one.
    
    8. Payouts:
       - A Blackjack typically pays 3:2.
       - Regular wins pay 1:1.
       - If you and the dealer tie, it’s a "push," and no money is won or lost.

    '''
    return x