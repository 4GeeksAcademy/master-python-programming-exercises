import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function day_of_week must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.day_of_week)

@pytest.mark.it('Something went wrong! We tried to pass 56 as parameter and it did not return 3!Keep trying!')
def test_for_file_output(capsys, app):

    assert app.day_of_week(56) == (3+56)%7

