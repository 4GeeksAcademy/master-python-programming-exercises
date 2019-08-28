import io
import sys
import os
sys.stdout = buffer = io.StringIO()

import pytest
import app




@pytest.mark.it('Create 3 variables each with numbers as value')
def test_for_variables(capsys):

    captured = buffer.getvalue()
    print(captured)

    assert app.a in globals()

    #assert type(app.a) is int
    #assert type(app.b) is int
    #assert type(app.c) is int


@pytest.mark.it('Add all three variables')
def test_add_variables(capsys):

    captured = buffer.getvalue()
    bb = captured.rstrip()
    result = app.a + app.b + app.c
    assert int(bb) == result
