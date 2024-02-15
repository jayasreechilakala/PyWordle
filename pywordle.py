import random
import requests

def generate_word():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'peach', 'pear', 'melon', 'lemon']
    return random.choice(words)

def is_valid_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}"
    response = requests.get(url)
    return response.status_code == 200

def check_guess(secret_word, guess):
    bulls = sum(1 for i in range(len(secret_word)) if secret_word[i] == guess[i])
    cows = sum(1 for letter in set(guess) if letter in secret_word and guess.count(letter) <= secret_word.count(letter)) - bulls
    return bulls, cows

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def main():
    secret_word = generate_word()
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("Welcome to Wordle!")
    print("Try to guess the 5-letter word. You have 6 attempts.")
    print("Make sure your guess is a valid English word.")
    
    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1}")
        guess = input("Enter your guess: ").lower()

        if len(guess) != len(secret_word):
            print("Invalid guess. Please enter a 5-letter word.")
            continue

        if not is_valid_word(guess):
            print("Invalid guess. Please enter a valid English word.")
            continue

        bulls, cows = check_guess(secret_word, guess)
        if bulls == len(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        print("Result:", bulls, "bull(s)", cows, "cow(s)")
        print("Word:", display_word(secret_word, guessed_letters))

        attempts += 1
        guessed_letters.update(guess)

    if attempts == max_attempts:
        print("Sorry, you've run out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    main()
