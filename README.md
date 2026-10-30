## Hangman in Python

### Features
- Configurable number of allowed incorrect guesses.
- Randomised word picked from 3 different categories.
- Word category display.
- Progress display.
- Regex validation of player inputs.
- TUI that should work on Windows and Linux (not tested on Windows).

Run the script in a terminal have fun.

### To do:
- Add a score counter and display a score summary at the end of the game.
- Handle player trying the same letter multiple times. Right now correct letter can be tried multiple times with no feedback and incorrect letter tried multiple times adds to incorrect guesses (debatable whether this is actually a problem).
- Introduce a win/loss condition and redo the game logic around it to make it clearer.
- Clean up code.