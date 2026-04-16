import pytest
from os import getenv

if getenv("TESTING") != "1":
    pytest.exit("Environment is not ready for tests.")