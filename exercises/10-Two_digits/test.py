import io, sys, pytest, os, re, mock

@pytest.mark.it('The function two_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.two_digits)

@pytest.mark.it('The function two_digits must return the left and right digits of a 2 digits integer')
def test_for_file_output(capsys, app):
    assert app.two_digits(30) == (30//10, 30%10)







