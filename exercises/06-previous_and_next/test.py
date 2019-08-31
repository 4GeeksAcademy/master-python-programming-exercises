import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable named number with any int as its value')
def test_for_variable(capsys):

    assert app.number is not None
    assert type(app.number) is int


@pytest.mark.it('Print next number')
def test_for_next_number(capsys):

    captured = buffer.getvalue()

    assert captured == str(app.number + 1) + "\n"

