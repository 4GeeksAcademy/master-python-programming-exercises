import io, sys, pytest, os, re, mock, app

# @pytest.mark.it('The function swap_digits must exist')
# def test_for_functon_existence():
#     assert callable(app.swap_digits)

@pytest.mark.it('The function swap_digits must exist')
def test_function_exists():
    assert app.swap_digits

@pytest.mark.it('The function swap_digits must return something')
def test_return_exists():
    assert app.swap_digits(12) != None

@pytest.mark.it('The function swap_digits should return an integer')
def test_return_integer():
    assert type(app.swap_digits(23)) == type(1)
    
@pytest.mark.it('If `swap_digits` recieve 30 should return 3')
def test_for_file_output(capsys, app):
    assert app.swap_digits(30) == 3

@pytest.mark.it('The function `swap_digits` must swap the digits')
def test_for_file_output(capsys, app):
    assert app.swap_digits(79) == 97 or app.swap_digits(79) == "97"