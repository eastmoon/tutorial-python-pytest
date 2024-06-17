# content of myinvoke.py
import sys

import pytest

if __name__ == "__main__":
    sys.exit(pytest.main(["test/test_case0.py"]))
