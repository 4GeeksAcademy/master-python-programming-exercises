import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function total_cost must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.total_cost)

@pytest.mark.it('We tried to pass 15, 22, 4 as parameters and it did not return (60, 88)!')
def test_for_file_output(capsys, app):

    assert app.total_cost(15, 22, 4) == ((((15*100)+22)*4)//100, (((15*100)+22)*4)%100)
  
