import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable named number with any int as its value')
def test_for_variable(capsys):

    assert app.number is not None
    assert type(app.number) is int


@pytest.mark.it('Print previous number')
def test_for_previous_number(capsys):

    captured = buffer.getvalue()
    print(captured)
    assert str(app.number + 1) + "\n" in captured

@pytest.mark.it('Print next number')
def test_for_next_number(capsys):

    captured = buffer.getvalue()
    print(captured)
    n = app.number
    assert str("The next number for the number" + n + "is" + n + 1) + "\n" in captured





