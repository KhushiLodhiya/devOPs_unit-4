# test_app.py

from app import add

def test_addition():
    a = 5
    b = 10
    assert add(a, b) == 10
