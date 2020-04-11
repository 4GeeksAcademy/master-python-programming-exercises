import io, sys, pytest, os, re, mock

@pytest.mark.it('The function  first_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.first_digit)

@pytest.mark.it('We tried to pass 6.24 as parameter and it did not return 2!')
def test_for_file_output(capsys, app):
    assert app.first_digit(6.24) == int(6.24 *10)%10

