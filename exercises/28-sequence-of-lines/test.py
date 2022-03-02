import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The solution should return the expected output')
def test_input_output(capsys, app):

    fake_input = ["Hello world Practice makes perfect"]
    with mock.patch('builtins.input', lambda x: fake_input.pop(0)):
        app()
        captured = capsys.readouterr()
        assert captured.out == "HELLO WORLD PRACTICE MAKES PERFECT\n"