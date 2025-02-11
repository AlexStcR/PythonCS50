import pytest
import fuel


from fuel import convert, gauge


def test_convert():
    assert convert("1/2")==50
    assert convert("1/4")==25

def test_errors():
    with pytest.raises(ValueError):
        convert ("dog/cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1)=="E"
    assert gauge(100)=="F"
    assert gauge (50)=="50%"
    assert gauge(99)=="F"

