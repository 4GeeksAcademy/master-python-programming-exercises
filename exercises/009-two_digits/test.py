import io, sys, pytest, os, re, mock

@pytest.mark.it('The function two_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.two_digits)

@pytest.mark.it('The function must return something')
def test_function_return(capsys, app):
    assert app.two_digits(30) != None

@pytest.mark.it('The function must return a tuple')
def test_function_return_type(capsys, app):
    result = app.two_digits(30)
    assert type(result) == type((1,2))

@pytest.mark.it('The function must return a tuple with numbers')
def test_for_file_output(capsys, app):
    result = app.two_digits(30)
    assert type(result[0]) == type(1) and type(result[1]) == type(1)

@pytest.mark.it('The function two_digits must return the left and right digits of a 2 digits integer')
def test_for_file_output(capsys, app):
    assert app.two_digits(30) == (3,0)

@pytest.mark.it('The function two_digits must return the left and right digits of a 2 digits integer. Testing with 45')
def test_for_file_output(capsys, app):
    assert app.two_digits(45) == (4,5)







