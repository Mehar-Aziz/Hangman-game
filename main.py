import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

lives = 6

display = []
guess_words = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in guess_words:
        print(f"The letter {guess} is already guessed")
    else:
        guess_words.append(guess)
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the Word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])

