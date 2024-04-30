import time
import pytest


@pytest.mark.slow  # "slow" could be any name you want to use
def test_slow_marker():
    time.sleep(2)  # Simulate a slow test; in this case, 10 seconds
