import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create three variables(a,b,n) and give it any interger as its value')
def test_for_variables(capsys):

    assert app.a is not None
    assert type(app.a) is int
    assert app.b is not None
    assert type(app.b) is int
    assert app.n is not None
    assert type(app.n) is int


@pytest.mark.it('Print total cost in dollars and cents.')
def test_for_dollars_and_cents(capsys):
    captured = buffer.getvalue()
    a = int(10)
    b = int(15)
    n = int(2)

    Total_cost_dollar= (n*a)
    Total_cost_cents= (n*b)
    assert captured == str(Total_cost_dollar) + " " + str(Total_cost_cents) + "\n"



