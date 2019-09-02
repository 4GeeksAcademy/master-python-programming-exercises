import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" with any interger as its value')
def test_for_variable(capsys):

    captured = buffer.getvalue()

    assert app.num is not None
    assert type(app.num) is int

@pytest.mark.it("Print its tens digit")
def test_for_tens_digit(capsys):

    captured = buffer.getvalue()

    import math

    app.num
    b = math.floor((app.num / 10) % 10)

    assert captured == str(b) + "\n"
