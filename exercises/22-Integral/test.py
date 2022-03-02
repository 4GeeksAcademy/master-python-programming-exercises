import pytest,os,re,io,sys, mock, json


@pytest.mark.it('Almost there! But you need to convert the incoming input from string to integer')
def test_convert_inputs(capsys, app):

    fake_input = ["8"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n"


@pytest.mark.it('Almost there! But you need to convert the incoming input from string to integer')
def test_convert_inputs_2(capsys, app):

    fake_input = ["5"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"


