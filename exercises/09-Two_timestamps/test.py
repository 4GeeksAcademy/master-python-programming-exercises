import io
import sys
sys.stdout = buffer = io.StringIO()


import app
import pytest

@pytest.mark.it('Create 6 variables with intergers as its values')
def test_create_6_variables(capsys):

    captured = buffer.getvalue

    assert app.hour_1 is not None
    assert type(app.hour_1) is int
    assert app.hour_2 is not None
    assert type(app.hour_2) is int
    assert app.min_1 is not None
    assert type(app.min_1) is int
    assert app.min_2 is not None
    assert type(app.min_2) is int
    assert app.sec_1 is not None
    assert type(app.sec_1) is int
    assert app.sec_2 is not None
    assert type(app.sec_2) is int


@pytest.mark.it('print desired out per example')
def test_for_output(capsys):

    captured = buffer.getvalue()
    a = (app.hour_2 - app.hour_1) * 3600
    b = (app.min_2 - app.min_1) * 60
    c = app.sec_2 - app.sec_1
    d = a + b + c

    assert captured == str(d) + "\n"










