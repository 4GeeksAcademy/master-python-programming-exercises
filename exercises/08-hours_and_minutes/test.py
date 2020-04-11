import io, sys, pytest, os, re, mock

@pytest.mark.it('The function hours_minutes must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.hours_minutes)

@pytest.mark.it('The function hours_minutes must return the correct output')
def test_for_file_output(capsys, app):
    assert app.hours_minutes(4004) == (4004//3600, 4004//60)





