import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create three variables with the right values')
def test_for_variables(capsys):

    captured = buffer.getvalue()
    print(captured)

    assert app.a is not None
    assert type(app.a) is int
    assert app.b is not None
    assert type(app.b) is int
    assert app.c is not None
    assert type(app.c) is int


@pytest.mark.it('Create three variables with the right values')
def test_for_file_output(capsys):

    captured = buffer.getvalue()

    assert captured == str(app.b) + " " + str(app.c) + "\n"

