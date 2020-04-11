import io, sys, pytest, os, re, mock

@pytest.mark.it('The function previous_next must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.previous_next)

@pytest.mark.it('The function previous_next must return the correct output')
def test_for_file_output(capsys, app):
    assert app.previous_next(6) == (5, 7)







