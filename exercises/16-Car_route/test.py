import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create two variables (n and m) and give it any interger as its value')
def test_for_variable(capsys):

    captured = buffer.getvalue()

    assert app.n is not None
    assert type(app.n) is int
    assert app.m is not None
    assert type(app.m) is int



@pytest.mark.it('Print how many days will it take to cover the route of length M kilometers')
def test_for_days_to_cover_route(capsys):

    captured = buffer.getvalue()

    import math

    n = app.n
    m = app.m
    d = math.ceil(m/n)

    assert captured == str(d) + "\n"



