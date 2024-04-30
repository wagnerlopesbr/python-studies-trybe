def test_faker_last_name(faker):
    fake_last_name = faker.last_name()
    assert isinstance(fake_last_name, str)
    # assert fake_last_name.isalpha()   # This line is commented out because the faker.last_name() method may return a string with spaces, hyphens, or other characters that are not letters that would crash the test.


def test_faker_email(faker):
    fake_email = faker.email()
    assert isinstance(fake_email, str)
    assert "@" in fake_email
    assert "." in fake_email


def test_faker_password(faker):
    fake_password = faker.password()
    valid_symbols = "!@#$%^&*()_+"
    assert isinstance(fake_password, str)
    assert len(fake_password) >= 4
    assert any(char.isdigit() for char in fake_password)
    assert any(char in valid_symbols for char in fake_password)
