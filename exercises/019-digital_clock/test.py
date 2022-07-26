import io, sys, pytest, os, re, mock, math
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function digital_clock must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.digital_clock)

@pytest.mark.it('We tried to pass 194 as parameter and it did not return (3, 14)!Keep Trying!')
def test_for_file_output(capsys, app):

    assert app.digital_clock(194) == ((194 // 60), (194 % 60))

