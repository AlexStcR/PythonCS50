import pytest
import seasons


from seasons import check_format,pass_date, transform_date,minutes_to_words


def test_pass_date():
    assert pass_date("2000-10-10")==[2000, 10, 10]



def test_check_format():
    assert check_format("2000-10-10")=="2000-10-10"

def test_transform_date():
     assert transform_date([2000,10,10])==12813120


def test_minutes_to_words():
    assert minutes_to_words("12813120")=="Twelve million, eight hundred thirteen thousand, one hundred twenty minutes"
