import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The output should be the expected')
def test_output(capsys, app):
    fake_input = ["without,hello,bag,world"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "bag, hello, without, world\n"

@pytest.mark.it('Your solution should work with other entries')
def test_other_inputs(capsys, app):
    fake_input = ["hola,como,estas"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "como, estas, hola\n"