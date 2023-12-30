import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function day_of_week must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.day_of_week)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.day_of_week(1) != None

@pytest.mark.it('The function must return a number')
def test_function_return_type(capsys, app):
    assert type(app.day_of_week(1)) == type(1)

@pytest.mark.it('Something went wrong! We tried to pass 1 as parameter and it did not return 4. Keep trying!')
def test_for_file_output(capsys, app):
    assert app.day_of_week(1) == 4

@pytest.mark.it('Something went wrong! We tried to pass 46 as parameter and it did not return 0. Keep trying!')
def test_for_file_output2(capsys, app):
    assert app.day_of_week(46) == 0

