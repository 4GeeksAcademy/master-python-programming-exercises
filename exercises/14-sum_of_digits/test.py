import io
import sys
import os
sys.stdout = buffer = io.StringIO()

import app
#from app import digits_sum
import pytest



@pytest.mark.it('Create function digit_sum ')
def test_for_variable(capsys):

 assert app.digits_sum is not None

@pytest.mark.it('Print the sum of the digits')
def test_for_sum_of_digits(capsys):
    app.digits_sum(123)
    captured = capsys.readouterr()

    print(captured)
    if captured.out == str(6) + "\n":
        assert True
    else:
        assert False



