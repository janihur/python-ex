import pytest

def test_even():
    from src.intseqs import even

    try:
        even(0)
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert str(ex) == "n must be a positive integer."

    assert even(1)  == [0]
    assert even(2)  == [0, 2]
    assert even(10) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def test_1_fibonacci1():
    from src.intseqs import fibonacci1
    
    try:
        fibonacci1(0)
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert str(ex) == "n must be a positive integer."

@pytest.mark.parametrize(
    "n, expected", [
    (1,  [0]),
    (2,  [0, 1]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_2_fibonacci1(n, expected):
    from src.intseqs import fibonacci1

    assert fibonacci1(n) == expected
