import pytest


def test_add():
    assert 2 == 2

def name(name1):
    return name1

obj = name("swetha")
print(obj)


def test_name():
    assert name("swetha") == "swetha"
