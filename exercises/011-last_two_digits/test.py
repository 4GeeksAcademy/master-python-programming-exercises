import io, sys, pytest, os, re, mock

@pytest.mark.it('The function last_two_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.last_two_digits)

@pytest.mark.it('The function last_two_digits must return only the last 2 digits of a integer greater than 9')
def test_for_file_output(capsys, app):
  if app.last_two_digits(30) > 9:
    assert app.last_two_digits(30) == int(str(30)[-2:])
  




