import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function two_digits is defined')
def test_for_function(capsys):
    assert app.two_digits is not None

@pytest.mark.it("Print the left right digit of any two digits number")
def test_for_left_and_right_digit(capsys):
    app.two_digits(23)
    captured = capsys.readouterr()

    assert captured.out == "2 " + "3" + "\n"


