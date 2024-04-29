import pytest


@pytest.fixture(scope="module")
def my_list():
    return [1, 2, 3]


def pytest_configure(config):  # to avoid @pytest.mark.slow warning in every test
    config.addinivalue_line("markers", "slow: mark test as slow")
