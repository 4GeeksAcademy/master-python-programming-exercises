import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable k and give it an interger between 1 and 365 as its value.')
def test_for_variable(capsys):

    assert app.k is not None
    assert type(app.k) is int
    assert app.k <= 365 and app.k > 0


@pytest.mark.it('Print the number of day of week for K-th day of year.')
def test_for_number_of_day_of_week(capsys):
    captured = buffer.getvalue()

    k = app.k
    dday=((3+k)%7)

    assert captured == str(dday) + "\n"

