import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('The solution should return the expected output')
def test_convert_inputs(capsys, app):

    fake_input = ["Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85"] #fake input
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]\n"