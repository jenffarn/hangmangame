# open text file containg the words and add them to an array
hangman_words = []

hangman_text = open("hangmanwordlist.txt")

for word in hangman_text:
    hangman_words.append(word.strip().lower())

hangman_text.close()

# make a function to return a string containing secret and guessed letters
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

# chose a random secret word from array
import random

secret_word = random.choice(hangman_words)
updated = ""
count = 0

# display secret word as string of "-"s
for i in range(len(secret_word)):
    updated = updated + "-"

print(updated)

# initialise array containing wrong guesses
wrong_list = []

# main program
while True:
    guess_letter = input("Guess a letter: ")
    guess_letter = guess_letter.lower()

    # catch cases of multiple letters or non letters
    if len(guess_letter) > 1 or guess_letter.isalpha() == False:
        print("Not a valid guess")
        continue
    
    # player guessed a wrong letter again
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
        print("you lost!") # player exceeded 10 wrong guesses
        print("The secret word is " + secret_word)
        break