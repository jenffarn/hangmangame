hangman_words = []

hangman_text = open("hangmanwordlist.txt")

for word in hangman_text:
    hangman_words.append(word.strip().lower())

hangman_text.close()

import random

def update_word(secret, show, guess):
    new = ""
    for i in range(len(secret)):
        if show[i] == "-":
            if guess == secret[i]:
                new = new + secret[i]
            else:
                new = new + "-"
        else:
            new = new + show[i]
    return new

secret_word = random.choice(hangman_words)
updated = ""
count = 0

for i in range(len(secret_word)):
    updated = updated + "-"

print(updated)

wrong_list = []

while True:
    guess_letter = input("Guess a letter: ")
    guess_letter = guess_letter.lower()

    if len(guess_letter) > 1 or guess_letter.isalpha() == False:
        print("Not a valid guess")
        continue
    
    if not guess_letter in secret_word:       
        if guess_letter in wrong_list:
            print("You have already guessed this letter")
        else:
            wrong_list.append(guess_letter)     
            count = count + 1

    updated = update_word(secret_word, updated, guess_letter)
    print(wrong_list)
    print(updated)
    
    if updated == secret_word:
        print("You won!")
        break
    elif count >= 10:
        print("you lost!")
        print("The secret word is " + secret_word)
        break