import io, sys, pytest, os, re, mock

@pytest.mark.it('The function two_timestamp must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.two_timestamp)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    result = app.two_timestamp(1,2,30,4,3,20)
    assert  result != None

@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
    result = app.two_timestamp(1,2,30,4,3,20)
    assert  type(result) == type(1)

@pytest.mark.it('We tried passing (1,2,30,4,3,20) as parameters and the function did not return 10850. Keep Trying!')
def test_for_file_output(capsys, app):
    assert app.two_timestamp(1,2,30,4,3,20) == ( (3 * 60) + (4 * 3600) + 20 )- ((2 * 60) + (1 * 3600) + 30)














