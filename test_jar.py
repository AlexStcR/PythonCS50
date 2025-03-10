from jar import Jar
import pytest

def test_str():
    jar=Jar()
    assert str(jar)== ""
    jar.deposit(5)
    assert str(jar)=="🍪🍪🍪🍪🍪"
def test_init():
    jar=Jar()
    assert jar.capacity==12
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test default capacity
    default_jar = Jar()
    assert default_jar.capacity == 12

def test_deposit():
    jar = Jar(10)

    # Valid deposits
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10

    # Test over-deposit
    with pytest.raises(ValueError):
        jar.deposit(1)

    # Test negative deposit
    with pytest.raises(ValueError):
        jar.deposit(-2)
def test_withdraw():
    jar = Jar(10)
    jar.deposit(8)

    # Valid withdrawals
    jar.withdraw(3)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0

    # Test over-withdrawal
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Test negative withdrawal
    with pytest.raises(ValueError):
        jar.withdraw(-2)



