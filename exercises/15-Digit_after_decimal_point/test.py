import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function first_digit is defined')
def test_for_function(capsys):
    assert app.first_digit is not None



@pytest.mark.it('Print the first digit to the right of the decimal point')
def test_first_digit_to_the_right_of_decimal_point(capsys):
    app.first_digit(4443.1)
    captured = capsys.readouterr()

    assert captured.out == "1" + "\n"

