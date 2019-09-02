import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" with an interger greater than 99 as its value')
def test_for_variable(capsys):

    assert app.num is not None
    assert type(app.num) is int
    assert app.num >= 100


@pytest.mark.it('Print the last two digits of num')
def test_for_output(capsys):

    captured = buffer.getvalue()
    b = str(app.num)
    assert captured == b[-2:] + "\n"

