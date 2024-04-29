import pytest
from testing_doctest_code01 import mean


@pytest.mark.parametrize(  # pytest decorator that allows us to pass multiple arguments to the test function so we won't need to create multiple assert statements
    "input, result",  # parameters names; you can name them whatever you want
    [
        ([1, 2, 3, 4, 5, 6, 7], 4.0),  # tuple with (input, expected) result
        ([2.5, 3.75, 1.25, 4], 2.875),
        ([], 0)
    ],
)
def test_parametrized_mean(input, result):
    assert mean(input) == result
