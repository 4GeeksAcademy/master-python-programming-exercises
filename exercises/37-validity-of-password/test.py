import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('Your solution should work as expected')
def test_expected_output(capsys, app):
    fake_input=['ABd1234@1,a F1#,2w3E*,2We3345']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "ABd1234@1\n"

@pytest.mark.it('Your solution should work as expected for valid passwords')
def test_expected_another_output(capsys, app):
    fake_input=['Lmd4567@2,a F1#,2w3E*,2We3345']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "Lmd4567@2\n"

@pytest.mark.it('Your solution should work as expected when there is no valid password input')
def test_expected_output_no_valid_entries(capsys, app):
    fake_input=['ABd12,a F1#,2w3E*,2We3345']
    with mock.patch('builtins.input', lambda x: fake_input.pop()):
        app()
        captured = capsys.readouterr()
        assert captured.out == "\n"