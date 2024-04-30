# Testing2 Studies

Commands to run tests:
- pytest --cov  /// comment: to run all test files only with STMTS (statements), MISS and COVER columns
- pytest --cov "folder_or_file_name"  /// comment: to run "file_name", module or package -> "pytest --cov tests" (run all files inside the "tests" folder)
- pytest --cov --cov-report=term-missing    /// comment: to run all test files
- pytest --cov "folder_or_file_name" --cov-report=term-missing  /// comment: to run all specific folder or file