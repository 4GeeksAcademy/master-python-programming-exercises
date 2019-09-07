import io
import sys
import os
sys.stdout = buffer = io.StringIO()

import app
from app import digits_sum
import pytest



@pytest.mark.it('Create variable "three_digit_number" with a three digit int as its value')
def test_for_variable(capsys):

    assert app.three_digit_number is not None
    assert type(app.three_digit_number) is int
    assert app.three_digit_number > 99
    assert app.three_digit_number < 1000

@pytest.mark.it('Print the sum of the digits')
def test_for_sum_of_digits(capsys):
    digits_sum(123)
    captured = capsys.readouterr()

    print(captured)
    if captured.out == str(6) + "\n":
        assert True
    else:
        assert False

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    #assert captured == str(total) + "\n"
    assert content.find("print(total)") > 0


