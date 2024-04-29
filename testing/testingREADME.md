# Testing Studies

Commands to run doctests:
- python3 -m doctest "file_name".py
- pytest --doctest-modules -vv

Commands to run pytests:
- pytest "file name".py          /// comment: if you have 4 files starting with "testing_" you can type "pytest testing_*.py" to run all files starting with "testing_"; same case for files ending with same name -> "pytest *_code.py"
- pytest "file name".py -vv         /// comment: more detailed log
- pytest -m 'not slow' "file name".py -vv         /// comment: "slow" could be any name you want to use; depends on @pytest.mark."arg" (in this case -> arg = slow)