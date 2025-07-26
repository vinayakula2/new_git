import pytest

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def test_add():
    assert add(1 , 2) == 3
    assert add(2,4) != 4
    assert add(3,6) == 9

def test_sub():
    assert sub(1,3) == -2
    assert sub(2,6) != 4