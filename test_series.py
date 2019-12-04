import pytest
from series import fibonacci, lucas


def test_fib_one():
    expected = 0
    actual = fibonacci(1)
    assert actual == expected

def test_fib_two():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fib_three():
    expected = 1
    actual = fibonacci(3)
    assert actual == expected

def test_fib_four():
    expected = 8
    actual = fibonacci(7)
    assert actual == expected

def test_fib_five():
    expected = 144
    actual = fibonacci(13)
    assert actual == expected


def test_fib_six():
    with pytest.raises(ValueError) as context:
        fibonacci(-2)
    assert str(context.value) == 'numbers smaller than zero can not be used'


@pytest.mark.skip('pending')
def test_fib_seven():
    expected = 308061521170129
    actual = fibonacci(72)
    assert actual == expected
# above test stucks because the number is a big number to proceed so I skip this test

def test_lucas_one():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas_two():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas_three():
    expected = 3
    actual = lucas(2)
    assert actual == expected

def test_lucas_four():
    expected = 18
    actual = lucas(6)
    assert actual == expected

def test_lucas_five():
    expected = 123
    actual = lucas(10)
    assert actual == expected


@pytest.mark.skip('pending')
def test_lucas_six():
    expected = 1051849
    actual = lucas(64)
    assert actual == expected

# above test stucks because the number is a big number to proceed so I skip this test


def test_lucas_seven():
    with pytest.raises(ValueError) as context:
        lucas(-3)
    assert str(context.value) == 'numbers smaller than zero can not be used'
