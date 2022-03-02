import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('Your solution should work as expected')
def test_expected_output(capsys, app):
    fake_input=['ABd1234@1,a F1#,2w3E*,2We3345']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "ABd1234@1\n"