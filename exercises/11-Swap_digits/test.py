import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" with any interger greater than 10 as its value')
def test_for_variable(capsys):

    assert app.num is not None
    assert app.num >= 10
    assert type(app.num) is int


@pytest.mark.it('Swap digits')
def test_for_swapped_digits(capsys):

    captured = buffer.getvalue()

    first = app.num // 10
    second = app.num % 10
    swapped = (second * 10) + first

    assert captured == str(swapped) + "\n"

