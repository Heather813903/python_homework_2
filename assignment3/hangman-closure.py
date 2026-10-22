# Task 4

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""

        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"

        print(display_word)
        if "_" not in display_word:
            return True
        else:
            return False

    return hangman_closure

# Start the Hangman game
secret_word = input("Enter the secret word: ")
game = make_hangman(secret_word)

finished = False

while not finished:
    letter = input("Guess a letter: ")
    finished = game(letter)

print("You guessed the word!")