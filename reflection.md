# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

## Glitch 2: Higher/Lower Hints Are Reversed

### Investigation

While reviewing the game behavior and source code, I found that the Higher/Lower hint logic is reversed.

If the player's guess is greater than the secret number, the game should tell the player to guess LOWER.

If the player's guess is less than the secret number, the game should tell the player to guess HIGHER.

However, the current implementation associates the comparison with the wrong message.

### Expected behavior

- Guess < secret → "Go HIGHER!"
- Guess > secret → "Go LOWER!"

### Actual behavior

The game can give the opposite instruction, which makes the hint misleading and can send the player farther away from the correct answer.

### Initial hypothesis

The conditional comparisons themselves are understandable, but the hint messages connected to those conditions appear to have been reversed.

## Glitch 3: Game State Behavior Needs Verification

The project description indicates that the secret number may reset when Streamlit reruns the application after a button click.

Streamlit reruns the Python script whenever the user interacts with widgets, so values that need to persist between interactions should normally be stored in session state.

During my initial test, I was able to correctly guess the displayed secret number, so I did not assume that the secret-reset bug occurred in every run. I marked this behavior for further verification before modifying the code.

## Phase 1 Conclusion

This investigation showed why verification is important when working with AI-generated code. I did not assume that every documented bug would reproduce exactly the same way. I compared the visible behavior with the expected behavior and used human judgment before planning any changes.

The main issues identified for further investigation and repair are:

1. Inconsistent debug information after state updates.
2. Incorrect Higher/Lower hint behavior.
3. Potential problems with persistent Streamlit game state.
4. Score and attempt calculations that need verification.

This completes my initial Glitch Hunt before making repairs.

