import io, sys, pytest, os, re, mock

@pytest.mark.it('The function hours_minutes must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.hours_minutes)
    
@pytest.mark.it('The function hours_minutes must return the correct output for 60 secs')
def test_for_file_output(capsys, app):
    assert app.hours_minutes(60) == (0, 1)

@pytest.mark.it('The function hours_minutes must return the correct output for 3900 secs')
def test_for_file_output(capsys, app):
    assert app.hours_minutes(3900) == (1, 5)


@pytest.mark.it('The function hours_minutes must return the correct output for 4500 secs')
def test_for_file_output(capsys, app):
    assert app.hours_minutes(4500) == (1, 15)


@pytest.mark.it('The function hours_minutes must return the correct output for 7320 secs')
def test_for_file_output(capsys, app):
    assert app.hours_minutes(7320) == (2, 2)







