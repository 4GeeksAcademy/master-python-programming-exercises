import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("You need to use the print() method")
def test_use_print():
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"print(\s)*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The solution should return the expected output. Tested with 2, 3, 6')
def test_sum_expected_inputs(capsys, app):

    fake_input = ["2","3","6"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "11\n"

@pytest.mark.it('The solution must sum all entries. Tested with 0, 3, 7')
def test_sum_another_inputs(capsys, app):

    fake_input = ["0","3","7"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "10\n"

@pytest.mark.it('The solution must sum all entries. Tested with 0, 0, 0')
def test_sum_with_zero(capsys, app):

    fake_input = ["0","0","0"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "0\n"




