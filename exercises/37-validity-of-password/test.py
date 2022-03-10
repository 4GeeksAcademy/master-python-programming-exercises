import pytest, io, sys, json, mock, re, os
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('The function valid_password must exist')
def test_function_existence(capsys, app):
    assert app.valid_password

@pytest.mark.it('The function should return the expected output')
def test_expected_output(capsys, app):
    assert app.valid_password("ABd1234@1,a F1#,2w3E*,2We3345") == "ABd1234@1"

@pytest.mark.it('Your solution should work as expected for valid passwords')
def test_expected_another_output(capsys, app):
    assert app.valid_password("Lmd4567@2,a F1#,2w3E*,2We3345") == "Lmd4567@2"

@pytest.mark.it('Your solution should work as expected when there is no valid password input')
def test_expected_output_no_valid_entries(capsys, app):
    assert app.valid_password("ABd12,a F1#,2w3E*,2We3345") == ""