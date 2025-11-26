from app import run
import pytest

@pytest.mark.skip(reason="don't run slow tests every time")
def test_run_1():
    result = run(' foo ', ' bar ')
    assert result == "(foo True)(bar True)"

def test_run_2(mocker):
    # note the correct name of is_foo() is app.is_foo
    mocker.patch('app.is_foo', return_value = False)
    mocker.patch('app.is_bar', return_value = False)

    result = run('foo', 'anything goes!')
    assert result == "(foo False)(bar False)"

# this is also slow test because is_foo() is not mocked but impl_()
def test_run_3(mocker):
    # note the correct name of impl_() is lib.impl_
    mocker.patch('lib.impl_', side_effect = ['FOO', 'BAR'])
    result1 = run('foo', 'bar')
    assert result1 == "(foo True)(bar True)"

    mocker.patch('lib.impl_', side_effect = ['X', 'BAR'])
    result2 = run('FOO', 'BAR')
    assert result2 == "(foo False)(bar True)"