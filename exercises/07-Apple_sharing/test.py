import io
import sys
sys.stdout = buffer = io.StringIO()
import math
import app
import pytest

@pytest.mark.it('Create two variables with any interger as its value')
def test_for_variables(capsys):

    captured = buffer.getvalue()

    assert app.n is not None
    assert type(app.n) is int
    assert app.k is not None
    assert type(app.k) is int


@pytest.mark.it('Print output per example')
def test_for_output(capsys):

    captured = buffer.getvalue()

    assert str(app.k % app.n) + "\n" in captured
    assert str(math.floor(app.k / app.n)) + "\n" in captured