# Hangman Game

This is a Python implementation of the classic Hangman game. The player tries to guess the hidden word by suggesting letters within a certain number of guesses.

## Overview

The Hangman game randomly selects a word from a predefined list, and the player attempts to guess the word one letter at a time. The player has a limited number of incorrect guesses (lives), and the game provides visual feedback in the form of a hangman drawing.

## How to Play

1. The game randomly selects a word from the `word_list`.
2. The player guesses letters one by one.
3. If the guessed letter is in the word, the corresponding blanks are filled with the letter.
4. If the guessed letter is not in the word, the player loses a life.
5. The game ends when:
   - The player correctly guesses all the letters in the word.
   - The player runs out of lives.

## Files

- `hangman_words.py`: Contains the list of words from which the game randomly selects.
- `hangman_art.py`: Contains the stages of the hangman drawing and the game logo.
- `hangman.py`: The main game file containing the game logic.

## Prerequisites

- Python 3.x

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Mehar-Aziz/hangman-game.git
   cd hangman-game
2. **Run the code**
   ```sh
   python main.py