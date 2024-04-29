import pytest


def test_1():
    assert True


@pytest.mark.xfail  # this means the test is expected to fail
def test_2():
    assert False


@pytest.mark.skip(reason="testing skip reason argument")  # this means the test is skipped
def test_to_skip():
    assert True


def test_sum():
    assert sum([1, 2, 3]) == 6


def test_list_item_multiply():
    my_list = [1, 2, 3]
    assert [item * 3 for item in my_list] == [3, 6, 9]
