import io, sys, pytest, os, re, mock

@pytest.mark.it('The function swap_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.swap_digits)

@pytest.mark.it('The function swap_digits must swap the digits of a 2 digits integer')
def test_for_file_output(capsys, app):
    assert app.swap_digits(30) == str(30%10)+str(30//10)



