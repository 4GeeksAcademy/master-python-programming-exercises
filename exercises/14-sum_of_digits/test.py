import io
import sys
import os
sys.stdout = buffer = io.StringIO()

import app
#from app import digits_sum
import pytest


@pytest.mark.it('Function digits_sum is defined')
def test_for_function(capsys):

 assert app.digits_sum is not None

@pytest.mark.it('Print the sum of the digits')
def test_for_sum_of_digits(capsys):
    app.digits_sum(123)
    captured = capsys.readouterr()

    print(captured)
    assert captured.out == str(6) + "\n"




