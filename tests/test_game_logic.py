from logic_utils import (
    check_guess,
    get_hint_message,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    assert check_guess(50, 50) == "Win"


def test_guess_too_high():
    assert check_guess(60, 50) == "Too High"


def test_guess_too_low():
    assert check_guess(40, 50) == "Too Low"


def test_high_guess_tells_player_to_go_lower():
    outcome = check_guess(60, 50)
    assert get_hint_message(outcome) == "📉 Go LOWER!"


def test_low_guess_tells_player_to_go_higher():
    outcome = check_guess(40, 50)
    assert get_hint_message(outcome) == "📈 Go HIGHER!"


def test_parse_valid_guess():
    assert parse_guess("42") == (True, 42, None)


def test_parse_invalid_guess():
    ok, value, error = parse_guess("hello")
    assert ok is False
    assert value is None
    assert error is not None


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_first_attempt_win_score():
    assert update_score(0, "Win", 1) == 90
