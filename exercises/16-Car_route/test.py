import io
import sys
sys.stdout = buffer = io.StringIO()

import app
import pytest

@pytest.mark.it('Function car route is defined')
def test_for_variable(capsys):
    assert app.car_route is not None



@pytest.mark.it('Print how many days will it take to cover the route of length M kilometers')
def test_for_days_to_cover_route(capsys):
    app.car_route(450,1000)
    captured = capsys.readouterr()

    assert captured.out == str(3) + "\n"



