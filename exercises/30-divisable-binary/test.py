import pytest, io, sys, json, mock, re, os

@pytest.mark.it('Your solution should work as expected')
def test_expected_output(capsys, app):
    fake_input=['0100,0011,1010,1001']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "1010\n"

@pytest.mark.it('Your solution should work with other parameters')
def test_expected_output_2(capsys, app):
    fake_input=['0100,0011,1010,1001']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "1111,0000,0101\n"