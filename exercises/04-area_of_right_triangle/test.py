import io
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it('Create variables b and h with any int as its value')
def test_create_variables(capsys):

    captured = buffer.getvalue()


    assert app.b is not None
    assert type(app.b) is int
    assert app.h is not None
    assert type(app.h) is int

@pytest.mark.it('find the area of the right triangle')
def test_find_the_area(capsys):

    result = 0.5 * app.b * app.h

    captured = buffer.getvalue()

    assert captured == str(result) + "\n"


