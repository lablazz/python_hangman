# %% [markdown]
# Import Lib

# %%
import random
import os

# %% [markdown]
# Add some word to dataset

# %%
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    words = ['python', 'hangman', 'computer', 'programming', 'challenge']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

# %% [markdown]
# Call the game window

# %%
def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        clear_console()
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letter : " + " ".join(sorted(guessed_letters)))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            print("Wrong guess!")
            attempts -= 1
    
    print(f"Game Over! The word was: {word}")

# %%
if __name__ == "__main__":
    hangman()


