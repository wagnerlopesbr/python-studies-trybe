def my_function():
    return f"You typed {input('Enter a value: ')}."


def test_my_function(monkeypatch):
    def mock_input(_):  # "_" is a "empty placeholder" for the prompt because we don't need it
        return "Gabigol"

    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "You typed Gabigol."
