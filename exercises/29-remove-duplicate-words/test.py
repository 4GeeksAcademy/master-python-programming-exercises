import pytest, io, sys, json, mock, re, os

@pytest.mark.it('Your solution should work as expected')
def test_expected_output(capsys, app):
    fake_input=['Hola como Hola']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == " como \n"