
import pytest
x = int(input("Please enter your number"))

def func(x):
    return x+1

def test_func():
    assert func(x)==4

test_func()