import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function day_of_week is defined')
def test_for_function(capsys):
    assert app.day_of_week is not None


@pytest.mark.it('Print the number of day of week for K-th day of year.')
def test_for_number_of_day_of_week(capsys):
    app.day_of_week(4)
    captured = capsys.readouterr()

    assert captured.out == str(0) + "\n"

