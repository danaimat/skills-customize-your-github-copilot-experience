
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python that practices string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description

Implement a Hangman game where the program selects a secret word from a list and the player guesses letters until the word is completed or guesses run out.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list
- Prompt the player to guess one letter per turn
- Display the current progress using underscores for hidden letters
- Track letters that have already been guessed
- Count and display remaining incorrect attempts
- End with a win message when the word is fully guessed or a lose message when attempts are exhausted
- Example flow:
  - Secret word: `python`
  - Player guesses: `p`
  - Display: `p _ _ _ _ _`
  - Player guesses: `o`
  - Display: `p _ _ _ o _`
