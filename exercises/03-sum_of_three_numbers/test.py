import io
import sys

sys.stdout = buffer = io.StringIO()

import pytest
import app


@pytest.mark.it('Create 3 variables each with numbers as value')
def test_for_file_output(capsys):

    captured = buffer.getvalue()
    print(captured)

    assert app.m is not None



@pytest.mark.it('Add all three variables')
def test_add_variables(capsys):

    captured = buffer.getvalue()
    bb = captured.rstrip()
    result = app.a + app.b + app.c
    assert int(bb) == result
