import io, sys, pytest, os, re, mock

@pytest.mark.it('The function previous_next must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.previous_next)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.previous_next(6) != None

@pytest.mark.it('The function should return a tuple')
def test_function_return_type(capsys, app):
    result = app.previous_next(6)
    assert type(result) == type((1,2))

@pytest.mark.it('The function previous_next must return the correct output')
def test_for_file_output(capsys, app):
    assert app.previous_next(6) == (5, 7)







