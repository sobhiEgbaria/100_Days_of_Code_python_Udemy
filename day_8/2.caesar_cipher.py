import caesar_module
from caesar_module import alphabet

play_again = True


def caesar(text, shift, direction):
    cipher_word = ""
    for latter in text:
        if latter not in alphabet:
            cipher_word += latter
            continue
        letter_index = alphabet.index(latter)
        if direction == "encode":
            if letter_index + shift < len(alphabet):
                cipher_word += alphabet[letter_index + shift]
            else:
                cipher_word += alphabet[letter_index + shift - (len(alphabet))]
        else:
            cipher_word += alphabet[letter_index - shift]
    print(cipher_word)


while play_again:
    print(caesar_module.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)

    caesar(text, shift, direction)
    keep_play = input('wanna play again? "yes" to play >>> Any key to exit:\n ').lower()
    if keep_play != "yes":
        play = False
