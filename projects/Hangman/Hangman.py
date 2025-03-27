import random as r
import HGman as H
def main():
    print("WELCOME TO HANGMAN") #Heading
    randwrd = r.choice(H.words()) #chooses a random word
    wrd = []  #the real word
    for i in randwrd:
        wrd.append(i)    #list of characters in the word
    word = [] #list of characters we choose
    life = 0
    for i in range(len(wrd)):
        word.append("_")
    game(life,word,wrd,randwrd)
def game(life,word,wrd,randwrd):
    while True:
        if life < 6 and "_" in word:
            print(H.drawings()[life])
            pword = ""
            for i in word:
                pword = pword + i
            print(f"Revealed Characters: {pword}")
            cha = input("Guess a character: ").lower()
            if cha in wrd:
                word.pop(wrd.index(cha))
                word.insert(wrd.index(cha),cha)
                wrd[wrd.index(cha)] = "_"
            else:
                life += 1
        elif "_" not in word:
            print(f"The word was indeed {randwrd}")
            print("You Got it")
            break
        else:
            print(H.drawings()[-1])
            print("You failed to Guess the Word")
            print(f"The word was {randwrd}")
            break
    x = int(input("Wanna Play Again?\n[1]YES\n[2]NO\n"))
    if x == 1:
        game(life, word, wrd, randwrd)
    else:
        print("GAME OVER")
main()