import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The solution should work as expected')
def test_convert_inputs(capsys, app):

    fake_input = ["100,150,180"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "18,22,24\n"

@pytest.mark.it('The solution should work with other parameters')
def test_convert_inputs_2(capsys, app):

    fake_input = ["200,90,300"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "26,17,32\n"
