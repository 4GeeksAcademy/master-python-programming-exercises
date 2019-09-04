import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it('Create variable "num" and give it an interger greater than 0')
def test_for_file_variable(capsys):

    assert app.num is not None
    assert type(app.num) is int
    assert app.num > 0




@pytest.mark.it('Print the respective century')
def test_for_output(capsys):

    captured = buffer.getvalue()

    import math

    n = app.num

    d = math.ceil(n/100)

    assert captured == str(d) + "\n"

