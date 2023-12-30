import io, sys, pytest, os, re, mock

@pytest.mark.it('The function last_two_digits must exist')
def test_for_functon_existence(capsys, app):
  assert callable(app.last_two_digits)

@pytest.mark.it('The function must return something')
def test_for_return(capsys, app):
  assert app.last_two_digits(30) != None
  
@pytest.mark.it('The function must return a number')
def test_for_output_type(capsys, app):
  assert type(app.last_two_digits(30)) == type(1)
  
@pytest.mark.it('The function last_two_digits must return only the last 2 digits of an integer greater than 9')
def test_for_file_output(capsys, app):
  if app.last_two_digits(30) > 9:
    assert app.last_two_digits(30) == int(str(30)[-2:])
  




