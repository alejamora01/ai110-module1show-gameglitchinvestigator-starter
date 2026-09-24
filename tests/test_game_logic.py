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


def test_negative_number_parses_as_integer():
    assert parse_guess("-5") == (True, -5, None)


def test_decimal_input_is_rejected():
    ok, value, error = parse_guess("3.14")
    assert ok is False
    assert value is None
    assert error == "That is not a whole number."


def test_extremely_large_number_is_handled():
    large_value = "999999999999999999999"
    ok, value, error = parse_guess(large_value)
    assert ok is True
    assert value == int(large_value)
    assert error is None


def test_whitespace_only_input_is_rejected():
    ok, value, error = parse_guess("   ")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_large_guess_compares_correctly():
    assert check_guess(999999, 50) == "Too High"
