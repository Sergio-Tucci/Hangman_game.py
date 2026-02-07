import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6  # variable holds number of live we start

print(logo)

chosen_word = random.choice(word_list)  # pick a random word from the word list
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)  # length of the chosen word
for position in range(word_length):  # creates _, accordingly number of letters in chosen word
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False  # variable to control when the game should stop
correct_letters = []  # list to save letters already guessed

while not game_over:  # loop to game repeating until vanish all the lives or guess the word wright

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()  # ask the user to guess a letter

    if guess in correct_letters:  # condition to check if the user is trying to guess a letter that he already guessed
        # without loosing life
        print(f"You've already guessed {guess}")  # when picked a letter already guessed, user doesn't lose life

    display = ""  # empty variable will show to user the spaces with underscore.

    for letter in chosen_word:  # loop through the chosen word
        if letter == guess:  # condition to see if the letter in the chosen word match guess letter.
            display += letter  # letter found in chosen word, display will receive the guess letter
            correct_letters.append(guess)  # append the correct letter to the list, saving for later
        elif letter in correct_letters:
            display += letter  # put the correct letter in the correct place to display again for the user
        else:
            display += "_"  # fill the spaces tha has not been filled by correct letter.

    print("Word to guess: " + display)  # show the correct letter for testing the code.

    if guess not in chosen_word:  # condition in case guess is not in the chosen word, user lose a life
        lives -= 1  # variable loses a life
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:  # condition in case life reaches 0 with means that user lost the game
            game_over = True  # variable becomes true to break while loop and end the program

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:  # condition to check if it has any underscore in display, no underscore means that the
        # user has won the game.
        game_over = True  # variable becomes true to break the while loop and end the game
        print("****************************YOU WIN****************************")

    print(stages[lives])  # print stages of the life.
