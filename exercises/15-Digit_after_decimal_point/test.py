import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" and give it a float interger as its value')
def test_for_variable(capsys):

    assert app.num is not None
    assert app.num > 0
    assert type(app.num) is float




@pytest.mark.it('Print its first digit to the right of the decimal point.')
def test_first_digit_to_the_right_of_decimal_point(capsys):

    import math
    captured = buffer.getvalue()

    a = app.num
    frac=math.modf(a)
    frac1=str(frac[0])

    assert captured == str(frac1[2]) + "\n"

