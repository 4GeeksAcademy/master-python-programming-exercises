import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Create variable n and give it any interger as its value')
def test_for_variable(capsys):

    assert app.n is not None
    assert type(app.n) is int
    assert app.hour is not None
    assert app.hour == app.n//60
    assert app.minute is not None
    assert app.minute == app.n % 60



@pytest.mark.it('Print hours and minutes displayed on the 24h digital clock.')
def test_for_hours_and_minutes(capsys):
    captured = buffer.getvalue()


    n = app.n

    hour = n//60
    minute = n % 60

    assert captured == str(hour) + " " + str(minute) + "\n"

