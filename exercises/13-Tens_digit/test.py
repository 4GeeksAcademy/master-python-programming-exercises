import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function tens_digit is defined')
def test_for_function(capsys):

    assert app.tens_digit is not None

@pytest.mark.it("Print the tens digit of a given number")
def test_for_tens_digit(capsys):
    app.tens_digit(343)
    captured = capsys.readouterr()

    assert captured.out == str(4) + "\n"
