import pytest
import numb3rs

from numb3rs import validate

def test_validate():
    assert validate("1.1.1.1")== True
    assert validate ("256.255.255.255")==False
    assert validate ("255.255.255.256")==False
    assert validate ("8.8.8")==False
    assert validate("cat")==False


