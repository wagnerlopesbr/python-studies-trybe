from create_user import create_user


def test_create_user(faker):
    fake_email = faker.email()
    fake_name = faker.name()
    result = create_user(fake_name, fake_email)
    assert fake_name.startswith(result["first_name"])
    assert fake_name.endswith(result["last_name"])
    assert fake_email == result["email"]
    assert fake_email.split("@")[-1] == result["email_domain"]
