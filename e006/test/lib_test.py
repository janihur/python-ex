'''
Example how to patch sut functions in tests.
'''

import lib # note how this defines the name you have to mock
import pytest

# "normal" test without mocking
# note also the processing delay
@pytest.mark.skip(reason="don't run slow tests every time")
def test_is_foo_1():
    assert lib.is_foo(' foo ') == True
    assert lib.is_foo('foo') == True
    assert lib.is_foo('bar') == False

# mocker is a "magic" pytest-mock fixture
# patch with return_value
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.return_value
def test_is_foo_2(mocker):

    mocker.patch(
        'lib.is_foo',
        return_value = True
    )
    assert lib.is_foo('anything goes!') == True

    mocker.patch(
        'lib.is_foo',
        return_value = False
    )
    assert lib.is_foo('nothing goes!') == False

# patch with side_effect list
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
def test_is_foo_3(mocker):

    mocker.patch(
        'lib.is_foo',
        side_effect = [True, False, True, ValueError('unexpected argument')]
    )

    assert lib.is_foo('first call') == True
    assert lib.is_foo('second call') == False
    assert lib.is_foo('third call') == True
    with pytest.raises(ValueError, match = 'unexpected argument'):
        lib.is_foo('fourth call')

# patch with side_effect function
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect
def test_is_foo_4(mocker):

    def side_effect(arg):
        if arg == 'a':
            return True
        elif arg == 'b':
            return False
        else:
            raise ValueError('unexpected argument c')

    mocker.patch(
        'lib.is_foo',
        side_effect = side_effect
    )

    assert lib.is_foo('a') == True
    assert lib.is_foo('b') == False
    with pytest.raises(ValueError, match = 'unexpected argument c'):
        lib.is_foo('c')