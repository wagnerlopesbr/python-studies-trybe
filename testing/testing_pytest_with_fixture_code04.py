import pytest


def test_1():
    assert True


@pytest.mark.xfail  # this means the test is expected to fail
def test_2():
    assert False


def test_sum(my_list: list[int]):
    assert sum(my_list) == 6


def test_list_item_multiply(my_list: list[int]):
    assert [item * 3 for item in my_list] == [3, 6, 9]
