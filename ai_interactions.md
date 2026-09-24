# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

## Challenge 1: Advanced Edge-Case Testing

### AI Prompt Used

I asked my AI coding assistant:

> Identify at least three edge-case inputs that could break or expose weaknesses in this number guessing game. Generate pytest tests for those cases and keep the tests simple and consistent with the existing `logic_utils.py` behavior.

### Edge Cases Chosen

1. **Negative number input (`-5`)**  
   I chose this case because negative integers are syntactically valid numbers even though they may fall outside the game's normal range. The test verifies that parsing still works consistently.

2. **Decimal input (`3.14`)**  
   I chose this case because the game expects whole-number guesses. The test verifies that decimal strings are rejected gracefully instead of causing a crash.

3. **Extremely large integer input**  
   I chose this case to verify that very large numeric strings can still be parsed safely by Python and handled by the comparison logic.

4. **Whitespace-only input**  
   I added this case because blank-looking input should be treated as missing input instead of being accepted or causing an exception.

5. **Extremely large guess comparison**  
   This verifies that the core comparison logic still returns `Too High` for a very large valid integer.

### Verification

I ran the complete pytest test set after adding the edge cases. I accepted the AI-generated test ideas because they were small, readable, and directly tested input parsing and comparison behavior without changing the game logic.
