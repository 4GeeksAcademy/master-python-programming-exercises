import io, sys, pytest, os, re, mock

@pytest.mark.it('The function swap_digits must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.swap_digits)

@pytest.mark.it('The function swap_digits must return something')
def test_for_functon_return_statement(capsys, app):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"return(\s*)[^a-zA-Z0-9_]\w+")
        assert bool(regex.search(content)) == True

    
@pytest.mark.it('If `swap_digits` recieve 30 should return 3 as an integer')
def test_for_file_output(capsys, app):
    assert app.swap_digits(30) == 3

@pytest.mark.it('The function `swap_digits` must swap the digits of a 2 digits integer')
def test_for_file_output(capsys, app):
    assert app.swap_digits(79) == 97



    

