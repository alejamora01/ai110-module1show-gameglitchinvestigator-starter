def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns:
        (ok, guess_int, error_message)
    """
    if raw is None or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a whole number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """Compare the guess with the secret number."""
    # FIXME: The original AI-generated version reversed Higher/Lower hints.
    # FIX: Refactored with AI assistance and verified with pytest.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome: str):
    """Return the player-facing hint for a guess outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on the outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points

    return current_score
