import twttr

from twttr import shorten

def test_shorten():
    assert shorten("twitter")=="twttr"
    assert shorten("TWITTER")== "TWTTR"

def test_shorten_numbers():
    assert shorten("1111")=="1111"

def test_shorten_ponctuation():
    assert shorten("%&!")=="%&!"






