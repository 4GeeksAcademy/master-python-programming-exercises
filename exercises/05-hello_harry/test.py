import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable name')
def test_create_variable(capsys):

    captured = buffer.getvalue()

    assert app.name is not None
    assert type(app.name) is str


@pytest.mark.it('Print output per example')
def test_desired_output(capsys):

    captured = buffer.getvalue()
    assert captured == "Hello, " + app.name + "!" + "\n"

