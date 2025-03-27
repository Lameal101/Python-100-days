import CaesarDrawings as d
def encrypt(word,shift):
    encrypted_text = ""
    for i in word:
        encrypted_text += chr(ord(i) + shift)
    return encrypted_text
def decrypt(word,shift):
    decrypted_text = ""
    for i in word:
        decrypted_text += chr(ord(i) - shift)
    return decrypted_text
def main():
    while True:
        choice = int(input("[1] Encrypt\n[2] Decrypt\n[3] Exit\n"))
        if choice == 1:
            word = input("Type the word:\n")
            shift = int(input("Type the shift:\n"))
            print(encrypt(word,shift))
        elif choice == 2:
            word = input("Type the word:\n")
            shift = int(input("Type the shift:\n"))
            print(decrypt(word, shift))
        elif choice == 3:
            break
        else:
            print("Type a correct number")
print(d.drawing())
main()