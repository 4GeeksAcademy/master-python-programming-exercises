import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function total_cost must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.total_cost)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.total_cost(15, 22, 4) != None
  
@pytest.mark.it('The function must return a tuple')
def test_function_return_type(capsys, app):
    assert type(app.total_cost(15, 22, 4)) == type((60, 88))
  
@pytest.mark.it('The function must return a tuple of numbers')
def test_function_return_type_parameters(capsys, app):
    result = app.total_cost(15, 22, 4)
    assert type(result[0]) == type(1) and type(result[1]) == type(1)
  
@pytest.mark.it('We tried to pass 15, 22, 4 as parameters and it did not return (60, 88)')
def test_for_file_output(capsys, app):
    assert app.total_cost(15, 22, 4) == (60, 88)
  
@pytest.mark.it('We tried to pass 10, 15, 4 as parameters and it did not return (40, 60)')
def test_for_file_output2(capsys, app):
    assert app.total_cost(10, 15, 4) == (40, 60)
  
