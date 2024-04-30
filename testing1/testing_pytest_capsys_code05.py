def test_print_to_stdout(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"  # print() automatically insert \n at the end


def test_error_to_stderr(capsys):
    import sys
    sys.stderr.write("Error")
    captured = capsys.readouterr()
    assert captured.err == "Error"
