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
    "paper",
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
    print(wrd)
    word = []
    life = 0
    for i in range(len(wrd)):
        word.append("_")
    while True:
        if life < 6 and "_" in word:
            print(HANGMANPICS[life])
            print(word)
            cha = input("Guess a character: ").lower()
            if cha in wrd:
                word.pop(wrd.index(cha))
                word.insert(wrd.index(cha),cha)
            else:
                life += 1
        elif "_" not in word:
            print("You Got it")
            break
        else:
            print("GAME OVER")
            break
main()