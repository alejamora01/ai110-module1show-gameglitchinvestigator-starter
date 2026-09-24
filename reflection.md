# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it opened correctly in Streamlit and allowed me to choose a difficulty, enter guesses, and see the Developer Debug Info. However, I noticed several logic and state problems while testing it. The biggest issues were incorrect Higher/Lower hints, inconsistent score/debug information after a correct guess, and incorrect attempt counting. I also reviewed the relevant code in `app.py` to connect each visible bug with a suspicious section of the implementation.

### Bug 1: Higher/Lower hints are reversed

**Input/Trigger:** Enter a guess that is lower or higher than the secret number.

**Expected behavior:** If the guess is lower than the secret, the game should say "Go HIGHER!". If the guess is higher than the secret, it should say "Go LOWER!".

**Actual behavior:** The game gives the opposite direction.

**Suspected code location:** `app.py`, function `check_guess()`. The messages associated with the `guess > secret` and `guess < secret` conditions are reversed.

### Bug 2: Debug score and history do not immediately match the result

**Input/Trigger:** I viewed the secret number in Developer Debug Info, entered the correct secret number `45`, and submitted the guess.

**Expected behavior:** The game should show the win and the Developer Debug Info should reflect the updated score and guess history.

**Actual behavior:** The game displayed "Correct!" and a final score of 70, but the Developer Debug Info still displayed `Score: 0` and `History: []` during that render.

**Suspected code location:** `app.py`, the order in which the Developer Debug Info is rendered compared with the later session-state updates inside the submit block.

### Bug 3: Attempts start at the wrong value

**Input/Trigger:** Start the game for the first time in Normal difficulty.

**Expected behavior:** Before making any guesses, attempts should start at 0 and all 8 attempts should be available.

**Actual behavior:** The session state initializes `attempts` to 1, so the interface can show only 7 attempts left before the player has actually used a guess.

**Suspected code location:** `app.py`, session state initialization where `st.session_state.attempts = 1`.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Guess lower than secret | Hint should say "Go HIGHER!" | Hint says "Go LOWER!" | none | `app.py`, `check_guess()` |
| Correct guess `45` | Win, score and history should all update consistently | Win shows final score 70, while debug panel still showed Score 0 and History [] | none | `app.py`, debug render and submit/session-state update order |
| Start Normal game before any guess | Attempts should start at 0 and show 8 attempts left | Attempts initialize at 1, effectively showing 7 attempts left | none | `app.py`, session-state initialization |

I did not fix these problems during Phase 1. My goal was to reproduce the behavior, document what I observed, and connect each symptom to the code before making changes.

---

## 2. How did you use AI as a teammate?

I used AI as a coding teammate to help isolate the game logic from the Streamlit UI. One suggestion I accepted was moving functions such as `check_guess`, `parse_guess`, difficulty range handling, and score logic into `logic_utils.py`. This was useful because it made the logic easier to read and test independently from the interface. I verified the refactor by running pytest and by launching the Streamlit app again.

Another AI suggestion needed modification instead of being accepted exactly as written. The initial repair approach focused on changing multiple parts of the app at once, but I wanted the fixes to remain simple and close to the starter structure. I kept the core refactor and bug fixes, but avoided adding unnecessary abstractions or extra files. I verified the final version by reviewing the diff, running the automated test set, and checking the behavior in the live game.

---

## 3. Debugging and testing your fixes

I fixed the reversed hint logic so that a guess above the secret returns `Too High` and tells the player to go lower, while a guess below the secret returns `Too Low` and tells the player to go higher. I also fixed the attempt counter so the game begins at 0 attempts instead of 1, and kept the secret value as an integer instead of changing its type on different attempts.

To verify the repairs, I added pytest cases in `tests/test_game_logic.py` for winning guesses, guesses that are too high or too low, hint messages, input parsing, difficulty ranges, and score behavior. I ran the complete test set with pytest and saved the output in `test_results.txt`. I also launched the Streamlit app again to confirm that the game still runs after the refactor.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
