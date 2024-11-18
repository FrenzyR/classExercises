from anothertest.main import suma

print(suma(2,2))

def test_1plus0():
    assert suma(1,0) == 1
    assert suma(0,1) == 1

def test_outro():
    assert suma(5, 4) == 9
