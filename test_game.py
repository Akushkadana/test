from game import check_guess


def test_win():
    assert check_guess(50, 50) == "WIN"


def test_number_is_less():
    assert check_guess(50, 30) == "LOW"


def test_number_is_greater():
    assert check_guess(50, 70) == "HIGH"


def test_wrong_data():
    try:
        check_guess(50, "abc")
        assert False
    except TypeError:
        assert True