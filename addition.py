def add(a, b):
    return a+b

def test_add(a, b):
    assert add(2, 3) == 5
    assert add(4, 5) == 9
    