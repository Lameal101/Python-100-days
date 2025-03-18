import random as r
words = [
    "magic",
    "bread",
    "chair",
    "dance",
    "eagle",
    "flour",
    "grape",
    "house",
    "knife",
    "lemon",
    "magic",
    "night",
    "ocean",
    "pear",
    "quiet",
    "river",
    "stone",
    "table",
    "unity",
    "violet"
]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def main():
    print("WELCOME TO HANGMAN")
    randwrd = r.choice(words)
    wrd = []
    for i in randwrd:
        wrd.append(i)
    word = []
    life = 0
    for i in range(len(wrd)):
        word.append("_")
    game(life,word,wrd,randwrd)
def game(life,word,wrd,randwrd):
    while True:
        if life < 6 and "_" in word:
            print(HANGMANPICS[life])
            pword = ""
            for i in word:
                pword = pword + i
            print(f"Revealed Characters: {pword}")
            cha = input("Guess a character: ").lower()
            if cha in wrd:
                word.pop(wrd.index(cha))
                word.insert(wrd.index(cha),cha)
            else:
                life += 1
        elif "_" not in word:
            print(f"The word was indeed {randwrd}")
            print("You Got it")
            break
        else:
            print('''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========''')
            print("You failed to Guess the Word")
            print(f"The word was {randwrd}")
            break
    x = int(input("Wanna Play Again?\n[1]YES\n[2]NO\n"))
    if x == 1:
        game(life, word, wrd, randwrd)
    else:
        print("GAME OVER")
main()