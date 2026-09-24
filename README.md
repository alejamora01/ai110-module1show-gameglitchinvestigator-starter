# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose

The purpose of this project was to investigate and repair an AI-generated number guessing game built with Streamlit. The game asks the player to guess a secret number while providing Higher/Lower hints and tracking attempts and score.

### Bugs Found

During testing, I identified several problems in the starter code. The Higher/Lower hints were reversed, the attempt counter started at the wrong value, and some game-state information did not update consistently. I also found logic that changed the type of the secret value during gameplay, which could create inconsistent comparisons.

### Fixes Applied

I refactored the core game logic from `app.py` into `logic_utils.py` so that it could be tested separately from the Streamlit interface. I corrected the Higher/Lower logic, fixed the attempt initialization, kept the secret number as an integer, improved the new-game reset behavior, and added automated pytest coverage for the repaired logic.

## 📸 Demo Walkthrough

1. The user launches the Streamlit game and selects a difficulty.
2. The game creates a secret number and displays the allowed range and remaining attempts.
3. If the secret is 50 and the user enters 40, the game returns `Go HIGHER!`.
4. If the user then enters 70, the game returns `Go LOWER!`.
5. When the user enters 50, the game displays `Correct!`, updates the final score, and ends the game.
6. Selecting New Game resets the attempts, score, history, status, and secret number for another round.

## 🧪 Test Results

Automated tests were created in `tests/test_game_logic.py` to verify winning guesses, guesses that are too high or too low, hint messages, parsing, difficulty ranges, and scoring.

The full terminal output is saved in `test_results.txt`.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
