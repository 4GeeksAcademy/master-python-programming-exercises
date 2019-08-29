import io
import sys

sys.stdout = buffer = io.StringIO()

import pytest
import app



@pytest.mark.it('Create 3 variables each with numbers(interger) as value')
def test_for_file_output(capsys):

    captured = buffer.getvalue()
    print(captured)

    assert app.a is not None
    assert type(app.a) is int
    assert app.b is not None
    assert type(app.b) is int
    assert app.c is not None
    assert type(app.c) is int



@pytest.mark.it('Add all three variables')
def test_add_variables(capsys):

    captured = buffer.getvalue()
    print(captured)

    result = app.a + app.b + app.c

    assert captured == str(result) + "\n"

