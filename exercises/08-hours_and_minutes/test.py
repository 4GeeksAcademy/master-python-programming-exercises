import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest


@pytest.mark.it('Function is defined')
def test_for_function(capsys):
    assert app.hours_minutes is not None


@pytest.mark.it('Print Full Hours')
def test_for_hours(capsys):
    app.hours_minutes(5500)
    captured = capsys.readouterr()
    test1 = captured.out.split(" ")

    if test1[0] == "1":
        assert True
    else:
        assert False


@pytest.mark.it('Print Full Minutes')
def test_for_minutes(capsys):

    app.hours_minutes(5500)
    captured = capsys.readouterr()
    test1 = captured.out.split(" ")

    if test1[1] == "91" + "\n":
        assert True
    else:
        assert False


