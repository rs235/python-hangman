## Hangman in Python

```
=========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

### Features
- Configurable number of allowed incorrect guesses.
- Randomised word picked from 3 different categories.
- Word category display.
- Progress display.
- Regex validation of player inputs (overkill but why not?).
- TUI that should work on Linux and Windows (not tested on Windows).

Run hangman.py in terminal and have fun.

### To do:
- Add a score counter and display a score summary at the end of the game.
- Handle player trying the same letter multiple times. Right now correct letter can be tried multiple times with no feedback and incorrect letter tried multiple times adds to incorrect guesses (debatable whether this is actually a problem).
- Introduce a win/loss condition and redo the game logic around it to make it clearer.
- Add ASCI art that changes to reflect the progress of the game. This could be incompatible with adjustable allowed incorrect guesses.