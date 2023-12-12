import io, sys, pytest, os, re, mock, app

@pytest.mark.it('The function swap_digits must exist')
def test_function_exists():
    assert app.swap_digits

@pytest.mark.it('The function swap_digits must return something')
def test_return_exists():
    assert app.swap_digits(12) != None

@pytest.mark.it('The function swap_digits should return an integer')
def test_return_integer():
    assert type(app.swap_digits(23)) == type(1)
    
@pytest.mark.it('The function swap_digits must swap the digits. Testing with 79')
def test_for_file_output(capsys, app):
    assert app.swap_digits(79) == 97

@pytest.mark.it('The function swap_digits must swap the digits. Testing with 30')
def test_for_file_output_2(capsys, app):
    assert app.swap_digits(30) == 3
