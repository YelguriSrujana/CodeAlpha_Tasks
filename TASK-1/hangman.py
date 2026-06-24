import random

words = ["python", "computer", "keyboard", "programming", "internship"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)