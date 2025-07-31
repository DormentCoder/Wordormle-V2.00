import time
import random

def load_words(filename):
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return words
# This is a defined function that picks any word located in 'dictionary.txt' with 5 characters

def get_feedback(guess, target):
    feedback = ['_'] * 5
    target_chars = list(target)
    guess_chars = list(guess)
    for i in range(5):
        if guess_chars[i] == target_chars[i]:
            feedback[i] = '*'
            target_chars[i] = None
            guess_chars[i] = None
    for i in range(5):
        if guess_chars[i] is not None and guess_chars[i] in target_chars:
            feedback[i] = '+'
            target_index = target_chars.index(guess_chars[i])
            target_chars[target_index] = None
    return ''.join(feedback)
# This is a definied fucntion that defines the rule conditions for each character displayed to the user, for instance '+' indicates that it is the correct letter in the wrong position

def main():
    words = load_words('dictionary.txt')
    target_word = random.choice(words)
    attempts = 6
    timer = 30
    start_time = time.time()
    # These are variables that are initialised within the main loop to reference within the game loop, such as the current time
    print("Welcome to Wordle!")
    print("Guess the 5 letter word. You have 6 attempts.")
    # Game Intro, prompts the user that the game has started
    for attempt in range(1, attempts + 1):
        while True:
            elapsed_time =  int(time.time() - start_time)
            time_remaining = timer - elapsed_time
            if time_remaining <= 0:
                print("Time's up! You ran out of time.")
                return
            # If the player runs out of time, then this condition will run; quitting the game
            print(f"Time left: {time_remaining}")
            guess = input(f"Attempt {attempt}: ").strip().lower()
            if guess == 'quit':
                print(f"You quit the game. The word was '{target_word}'.")
                return
            # If the player types in 'quit', then the game will end and the right word will be shown
            if len(guess) != 5:
                print("Please enter a 5 letter word.")
            # If the length of the guess isnt 5 characters long, then this condition will run
            elif guess not in words:
                print("Word not in dictionary. Try again.")
            # If the guess is not in the dictionary, then this condition will run
            else:
                break
            # If by any means, none of the above is valid, then the loop will continue to prompt the user to guess
        feedback = get_feedback(guess, target_word)
        print("Feedback:", feedback)
        if guess == target_word:
            print(f"Congratulations! You guessed the word '{target_word}' in {attempt} attempts.")
            break
        # If the player guesses the right word, then this condition will run and the game will end
    else:
        print(f"Sorry, the word was '{target_word}'.")
    # If the player runs out of attempts, then this condition will run and the game will end

if __name__ == "__main__":
    main()
# This function call will help the game to start