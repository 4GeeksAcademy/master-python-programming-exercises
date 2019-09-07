import io
import sys
import os
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
    num = app.num
    total = 0
    while(num>0):
        dig = num % 10
        total = total + dig
        num = num // 10

    print(total)

    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert captured == str(total) + "\n"
    assert content.find("print(total)") > 0
