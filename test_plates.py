import plates

from plates import is_valid


def test_2_letters():

     #“All vanity plates must start with at least two letters.”
     assert is_valid("SS")==True
     assert is_valid("C2")==False
     assert is_valid("2A")==False
     assert is_valid("44")==False






def test_number_characters():
    assert is_valid("CC")==True
    assert is_valid("CSCSCS")==True
    assert is_valid("C")==False
    assert is_valid("CSCSCSCSCS")==False


def test_number_in_middle():
     #“Numbers cannot be used in the middle of a plate; they must come at the end. For example,
     # AAA222 would be an acceptable …
     # vanity plate; AAA22A would not be acceptable.
     assert is_valid("AAA222")==True
     assert is_valid("AAA22A")==False
def test_no_zero():
     assert is_valid("CS05")==False
     assert is_valid("CS50")==True



def test_just_letters_and_numbers():
    #“No periods, spaces, or punctuation marks are allowed.”
    assert is_valid("PI3.14")==False
    assert is_valid("AA!AA")==False
    assert is_valid("A  A")==False





