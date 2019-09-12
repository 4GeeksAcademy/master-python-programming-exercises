import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function digital_clock is defined')
def test_for_function(capsys):
    assert app.digital_clock is not None


@pytest.mark.it('Print hours and minutes displayed on the 24h digital clock')
def test_for_hours_and_minutes(capsys):
    app.digital_clock(345)
    captured = capsys.readouterr()

    assert captured.out == str(5) + " " + str(45) + "\n"

