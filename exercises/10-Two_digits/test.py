import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable "num"')
def test_for_variable(capsys):

    assert app.num is not None
    assert type(app.num) is int

@pytest.mark.it("print the tens digit and the ones digit of the variable")
def test_for_output(capsys):

    captured = buffer.getvalue()


    assert captured == str(app.num//10) + " " + str(app.num%10) + "\n"


