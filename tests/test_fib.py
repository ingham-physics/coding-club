# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, and 4181
import pytest
from github_examples.fib import fib


def test_fib():

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(10) == 55

    with pytest.raises(ValueError):
        fib("asdkhjas")
