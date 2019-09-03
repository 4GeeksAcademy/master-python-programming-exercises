import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num" and "total"')
def test_for_variable(capsys):

    assert app.num is not None
    assert type(app.num) is int
    assert app.total is not None
    assert type(app.total) is int


@pytest.mark.it('Print the sum of the digits')
def test_for_sum_of_digits(capsys):
    captured = buffer.getvalue()


    n = app.num
    tot=0


    while(n>0):
        dig = app.dig
        tot=tot+dig
        n = n//10

    assert app.dig == app.num % 10
    assert captured == str(tot) + "\n"









