import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it('Function century is defined')
def test_for_function(capsys):
    app.century is not None



@pytest.mark.it('Print the respective century')
def test_for_output(capsys):
    app.century(1900)
    captured = capsys.readouterr()

    assert captured.out == str(19) + "\n"

