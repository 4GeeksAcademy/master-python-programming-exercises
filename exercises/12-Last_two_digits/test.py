import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function last_two_digits is defined')
def test_for_functions(capsys):

    assert app.last_two_digits is not None


@pytest.mark.it('Print the last two digits of an interger greater than 9')
def test_for_output(capsys):
    app.last_two_digits(2345)
    captured = buffer.getvalue()
    captured2 = capsys.readouterr()
    assert captured > str(9) + "\n"
    assert captured2 == str(45) + "\n"


