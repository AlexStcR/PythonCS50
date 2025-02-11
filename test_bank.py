import bank

from bank import value

def test_value():
    assert value("hello") == 0
    assert value ("hey")== 20
    assert value("What's up?")==100
def test_value_case():
    assert value("HelLo")== 0
    assert value("hOw aRe yoU DOING")==20
def test_value_phrase():
    assert value("How are you doing?")==20
    assert value("What's happening?")==100

