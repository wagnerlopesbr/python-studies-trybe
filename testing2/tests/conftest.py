import pytest


@pytest.fixture(scope="module", autouse=True)
def faker_seed():
    return "Trybe"


@pytest.fixture(scope="module", autouse=True)
def faker_locale():
    return "pt_BR"
