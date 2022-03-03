import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You need to use the print() method")
def test_use_print():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print(\s)*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('Almost there! But you need to convert the incoming input from string to integer')
def test_convert_inputs(capsys, app):

    fake_input = ["2","3","4"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out != "432\n"

@pytest.mark.it('Sum all three input numbers and print on the console the result')
def test_add_variables(capsys, app):

    fake_input = ["2","3","4"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "9\n"




